#!/usr/bin/env python3
"""Bluetooth auto-accept agent for headless A2DP sink (music-potato).

Registers as the default BlueZ agent with NoInputNoOutput capability so
Android (and any other device) can pair without entering a PIN. Also
auto-trusts every device after successful pairing so reconnects are instant.
"""
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s bt-auto-agent: %(message)s',
    stream=sys.stdout,
)
log = logging.getLogger()

AGENT_PATH = "/org/bluez/AutoAgent"
CAPABILITY = "NoInputNoOutput"


class AutoAgent(dbus.service.Object):
    @dbus.service.method("org.bluez.Agent1", in_signature="", out_signature="")
    def Release(self):
        log.info("Release")

    @dbus.service.method("org.bluez.Agent1", in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        log.info(f"AuthorizeService: {device} uuid={uuid} -> auto-accept")

    @dbus.service.method("org.bluez.Agent1", in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        log.info(f"RequestPinCode: {device} -> 0000")
        return "0000"

    @dbus.service.method("org.bluez.Agent1", in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        log.info(f"RequestPasskey: {device} -> 0")
        return dbus.UInt32(0)

    @dbus.service.method("org.bluez.Agent1", in_signature="ouq", out_signature="")
    def DisplayPasskey(self, device, passkey, entered):
        log.info(f"DisplayPasskey: {device} passkey={passkey}")

    @dbus.service.method("org.bluez.Agent1", in_signature="os", out_signature="")
    def DisplayPinCode(self, device, pincode):
        log.info(f"DisplayPinCode: {device} pin={pincode}")

    @dbus.service.method("org.bluez.Agent1", in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        log.info(f"RequestConfirmation: {device} passkey={passkey} -> auto-confirm")

    @dbus.service.method("org.bluez.Agent1", in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        log.info(f"RequestAuthorization: {device} -> auto-accept")

    @dbus.service.method("org.bluez.Agent1", in_signature="", out_signature="")
    def Cancel(self):
        log.info("Cancel")


def trust_device(bus, device_path):
    try:
        obj = bus.get_object("org.bluez", device_path)
        props = dbus.Interface(obj, "org.freedesktop.DBus.Properties")
        props.Set("org.bluez.Device1", "Trusted", dbus.Boolean(True))
        log.info(f"Trusted: {device_path}")
    except Exception as e:
        log.warning(f"Could not trust {device_path}: {e}")


def on_properties_changed(interface, changed, invalidated, path, bus):
    if interface != "org.bluez.Device1":
        return
    if "Paired" in changed and bool(changed["Paired"]):
        log.info(f"Device paired: {path} — trusting for auto-reconnect")
        trust_device(bus, path)


def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    agent = AutoAgent(bus, AGENT_PATH)
    manager = dbus.Interface(
        bus.get_object("org.bluez", "/org/bluez"),
        "org.bluez.AgentManager1",
    )
    manager.RegisterAgent(AGENT_PATH, CAPABILITY)
    manager.RequestDefaultAgent(AGENT_PATH)
    log.info(f"Agent registered at {AGENT_PATH} with capability {CAPABILITY}")

    bus.add_signal_receiver(
        lambda iface, changed, inv, path: on_properties_changed(iface, changed, inv, path, bus),
        dbus_interface="org.freedesktop.DBus.Properties",
        signal_name="PropertiesChanged",
        path_keyword="path",
    )

    GLib.MainLoop().run()


if __name__ == "__main__":
    main()
