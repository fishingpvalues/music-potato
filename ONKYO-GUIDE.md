# Onkyo TX-SR605 — Setup Guide
## Yamaha YST-FSW050 sub + Fluance ES1 towers + Le Potato
## NO REMOTE — front panel buttons only

---

## Read This First

### Front Panel Buttons Used in This Guide

```
[ STANDBY/ON ]                              — power on/off

[ DVD ] [ CBL/SAT ] [ GAME/TV ]             — HDMI inputs 1/2/3
[ CD ]  [ TAPE ]                            — optical inputs 1/2

[ MASTER VOLUME ]                           — large knob, left side

[ LISTENING MODE ◄ ] [ LISTENING MODE ► ]  — cycle listening modes
[ STEREO ]                                  — jump directly to Stereo mode

[ SETUP ]                                   — open/close setup menus
[ ▲ ] [ ▼ ] [ ◄ ] [ ► ]                   — navigate menus
[ ENTER ]                                   — confirm / enter submenu
[ RETURN ]                                  — go back one level

[ DIGITAL INPUT ]                           — assign digital inputs
[ TONE – ] [ TONE + ]                       — bass/treble (Stereo mode only)
```

### How SETUP menus work

```
Press [SETUP]       → menu opens (on TV screen if TV is connected, or on front display)
[▲][▼]             → scroll up/down through items
[ENTER]             → go into a submenu / confirm
[◄][►]             → change a value
[RETURN]            → go back one level
[SETUP] again       → exit all menus at any time
```

> **Tip — connect a TV first.** Plug a TV into Onkyo's **HDMI OUT** before setup. Full menus appear on screen, much easier than reading the tiny front panel display. Disconnect TV after setup if you don't need it.

### Critical facts about your hardware

**1. The ES1 towers need the sub.** Four 5-inch woofers roll off before 100 Hz. Without the sub active, your music has no bass.

**2. Never use Pure Audio mode.** It disables bass management entirely — sub gets zero signal with stereo music. Use **Direct** mode instead.

**3. Crossover = 80 Hz.** ES1 usable bass ends around 80–100 Hz. 80 Hz hands bass to the Yamaha sub cleanly. Setting it higher just works the sub harder; lower stresses the ES1 woofers.

**4. ES1 tweeter is bright.** Audioholics measurements show +3–6 dB peak from 5–20 kHz. Fix: −2 dB treble trim in Stereo mode. Direct mode has no tone controls — if brightness bothers you there, switch to Stereo.

---

## PHASE 1 — Before Powering On

Do all of this with the receiver off.

---

### 1. Place the ES1 Towers

The ES1 is rear-ported — it needs air behind it or bass goes boomy.

```
Back wall clearance:   60–90 cm minimum  (2–3 ft)
Side wall clearance:   60 cm minimum
Tweeter separation:    1.8–2.5 m apart
```

**Equilateral triangle:** distance between the two tweeters = distance from each tweeter to your listening position.

```
  [Left ES1] ←——— 2 m ———→ [Right ES1]
         \                  /
          \                /
           2 m          2 m
                 [You]
```

**Toe-in:** Point both speakers toward your listening position at **22–30°**. The ES1 tweeter is bright — less toe-in = softer treble. Start at 22°, adjust in 5° steps by ear after everything else is set.

---

### 2. Place the Yamaha Sub

**Best positions (try in this order):**
1. Along the front wall between the two ES1 towers — most integrated
2. Front corner (left or right of speakers) — more output, can sound boomy
3. Against a side wall — if corners are impractical

**Avoid:** inside a cabinet (blocks down-firing port), middle of the room, directly behind your listening position.

**Subwoofer crawl (optional but best method):**
1. Temporarily place the sub at your listening position (on the sofa/chair)
2. Play music with steady bass
3. Crawl around the floor near where the sub will normally live
4. The spot where bass sounds fullest and most even = where the sub goes
5. Move sub there

**Set the sub's physical knobs now:**

| Knob | Set to | Why |
|---|---|---|
| Volume | 50–60% | Starting point — you'll calibrate exactly via the receiver in Step 8 |
| Crossover | MAX (fully clockwise) | The Onkyo controls the crossover. Sub's own filter adds on top and causes problems. |
| Phase | 0° | Default. You'll test 0° vs 180° in Step 9 and pick whichever sounds fuller. |
| Power | ON | No auto-on on this sub. Leave it on whenever the Onkyo is in use. |

---

### 3. Wire the Speakers

```
Onkyo FRONT L terminals ──── Fluance ES1 Left   (red → red+, black → black−)
Onkyo FRONT R terminals ──── Fluance ES1 Right  (red → red+, black → black−)
```

**Polarity is critical.** Red to red, black to black on both speakers. Reversed polarity on one speaker cancels bass and makes the stereo image hollow.

**Check after wiring:** Play a podcast or spoken voice. The voice should sound solid and centred. If it sounds hollow, thin, or like it's coming from two places — one speaker is wired backwards, swap its two wires.

---

### 4. Wire the Subwoofer

```
Onkyo SUBWOOFER PRE OUT ──── single RCA cable ──── Yamaha YST-FSW050 LINE IN
```

One RCA cable, sub is mono. Do not use the sub's speaker-level inputs.

---

### 5. Connect Le Potato to the Onkyo

Pick one:

```
Option A (recommended): Le Potato HDMI out  ────  Onkyo HDMI IN 1
Option B (optical):     Le Potato TOSLINK   ────  Onkyo OPTICAL IN 1
```

---

### 6. Connect a TV for Menu Navigation (recommended)

```
Onkyo HDMI OUT  ────  TV HDMI IN
```

Full graphical menus appear on the TV screen. Without a TV you navigate by reading the Onkyo's own front panel display (abbreviated text, doable but harder). You can disconnect the TV after setup is complete.

---

## PHASE 2 — Receiver Setup (front panel buttons only)

Work through these steps **in order from top to bottom**.

---

### Step 1 — Power On

Press **[STANDBY/ON]**.

---

### Step 2 — Select Your Input

Press the input button for your Le Potato connection:

| Le Potato connected to | Press |
|---|---|
| HDMI IN 1 | **[DVD]** |
| HDMI IN 2 | **[CBL/SAT]** |
| HDMI IN 3 | **[GAME/TV]** |
| OPTICAL IN 1 | **[CD]** |
| OPTICAL IN 2 | **[TAPE]** |

Front panel display shows the selected input name.

**If display shows "NO SIGNAL"** after selecting an optical input:
```
Press [DIGITAL INPUT]
Press [◄][►] to cycle to: OPT 1 (or OPT 2 for optical in 2)
```
For HDMI inputs this is automatic — no assignment needed.

**What the display should show when signal is present:**
- `PCM` or `PCM 44.1K` / `PCM 48K` / `PCM 96K` = correct, lossless audio
- `DD` or `DTS` = problem on the Le Potato side (see Troubleshooting)

---

### Step 3 — Open Speaker Setup

```
Press [SETUP]
Press [▲][▼] to highlight "2. Speaker Setup"
Press [ENTER]
```

You are now in the Speaker Setup submenu. Stay here for Steps 4, 5, and 6.

---

### Step 4 — Set Speaker Config (crossover and subwoofer)

```
Press [▲][▼] to highlight "2. Speaker Config"
Press [ENTER]
```

Navigate each row with **[▲][▼]**, change values with **[◄][►]**:

| Row on screen | Set to | Notes |
|---|---|---|
| Subwoofer | **Yes** | Tells the receiver the sub is connected |
| Front | **80 Hz** | ES1 crossover — bass below 80 Hz goes to sub |
| Center | **None** | No centre speaker in this 2.1 setup |
| Surround | **None** | No surrounds |
| Surr Back | **None** | No surround back |
| LPF of LFE | **120 Hz** | Max frequency sent to sub from .1 channel |
| Double Bass | **Off** | Would add front channel bass to sub — wrong here |

When all values are set:
```
Press [RETURN]  →  back to Speaker Setup menu
```

---

### Step 5 — Set Speaker Distances

Measure the distance from your listening position (where your head is when seated) to each speaker with a tape measure.

```
Press [▲][▼] to highlight "3. Speaker Distance"
Press [ENTER]
```

Navigate with **[▲][▼]**, change values with **[◄][►]** (steps of 0.3 m / 1 ft):

| Row | What to enter |
|---|---|
| Front L | distance from your seat to Left ES1 tweeter (e.g. 2.4 m) |
| Front R | distance from your seat to Right ES1 tweeter (e.g. 2.4 m) |
| Subwoofer | distance from your seat to the Yamaha sub (e.g. 1.8 m) |
| Center / Surround / Surr Back | skip — set to None |

Accurate distances fix time alignment so all sounds arrive at your ears at the same moment.

```
Press [RETURN]  →  back to Speaker Setup menu
```

---

### Step 6 — Calibrate Speaker Levels

The receiver plays pink noise from each speaker one at a time. You adjust each channel's volume until all channels are equally loud at your seat.

```
Press [▲][▼] to highlight "4. Level Calibration"
Press [ENTER]
```

Pink noise starts playing from Front Left immediately.

**Navigation:**
- **[▲][▼]** — switch to the next speaker (pink noise moves to that speaker)
- **[◄][►]** — raise or lower that speaker's level (−12 to +12 dB; sub: −15 to +12 dB)

#### With a phone SPL meter app (recommended)

Download free: **NIOSH SLM** (Android + iOS, NIST-validated) or **Decibel X** (iOS) or **Sound Meter** (Android).

Set the app to: **C-weighting, Slow response** — do not use A-weighting, it gives wrong readings for this.

1. Place phone at ear height at your listening seat, mic pointing straight up
2. Pink noise is playing from **Front L** — adjust **[◄][►]** until app reads **75 dB**
3. Press **[▲][▼]** → now on **Front R** — adjust until app reads **75 dB**
4. Press **[▲][▼]** → now on **Subwoofer** — adjust until app reads **77–78 dB**

> Sub is set +2–3 dB above mains. In a 2.1 stereo setup the sub handles the bass from both channels combined, while each main speaker handles the full mid + treble range. The slight boost compensates for this asymmetry. This is not the +10 dB cinema LFE reference — that is for movies, not music.

| Speaker | Target | Starting point |
|---|---|---|
| Front L | **75 dB** | 0 dB, adjust ± |
| Front R | **75 dB** | 0 dB, adjust ± |
| Subwoofer | **77–78 dB** | +2 to +3 dB above fronts |

#### Without an SPL app (by ear)

1. Listen to pink noise from Front L — note its loudness
2. **[▲][▼]** → Front R — press **[◄][►]** until it sounds the same loudness as Front L
3. **[▲][▼]** → Subwoofer — leave at **0 dB** for now, fine-tune by ear in Step 10

```
Press [RETURN]  →  back to Speaker Setup menu
Press [RETURN]  →  back to main menu
```

---

### Step 7 — Turn Off Unnecessary Processing

```
Press [▲][▼] to highlight "4. Audio Adjust"
Press [ENTER]
```

Navigate with **[▲][▼]**, change with **[◄][►]**:

| Setting | Set to | Why |
|---|---|---|
| Dynamic EQ | **Off** | Boosts bass at low volume — useful for late-night TV, wrong for music |
| Dynamic Vol | **Off** | Auto volume levelling — kills dynamics in music |
| Re-EQ | **Off** | Softens harsh movie soundtracks — damages music |
| Late Night | **Off** | Compresses loud/quiet — useful for neighbours at 1am, wrong for music |

```
Press [SETUP]  →  exit all menus
```

---

### Step 8 — Select Listening Mode

No SETUP menu needed — use these buttons directly:

**To reach Direct:** Press **[LISTENING MODE ►]** repeatedly until display shows `DIRECT`
**To reach Stereo:** Press the **[STEREO]** button directly

---

#### When to use Direct

Direct disables all EQ and tone controls but keeps bass management fully active (sub gets the bass below 80 Hz). The signal goes from the input to the amplifier with as little processing as possible. This is what you want when the source is already good quality.

Use Direct when:
- Playing FLAC or ALAC files from MPD → Le Potato → Onkyo (this is the best-quality path you have)
- Listening via AirPlay 2 from iPhone/iPad
- Listening via Snapcast from the homelab
- Doing critical or attentive listening — sitting and actually listening, not background
- The volume is at 55 or above (loud enough that the ES1 tweeter brightness is not a problem)
- You are happy with how the ES1s sound — they are not fatiguing you

**What Direct does NOT do:** tone controls, loudness compensation, any EQ. What you hear is what came off the disc/file. If the ES1 tweeter bothers you in this mode, switch to Stereo — it's not a flaw in your setup, just the ES1's character.

---

#### When to use Stereo

Stereo keeps bass management active (sub works the same as Direct) but also activates tone controls. The only meaningful difference is that you can now use **[TONE –]** to trim the ES1's treble brightness by −2 dB.

Use Stereo when:
- The ES1s sound harsh, bright, or fatiguing in Direct mode — this is common at higher volumes
- Playing Spotify Connect (lossy OGG 320 kbps — EQ helps, can't hurt a lossy source)
- Background music while you're doing something else — you're not critically listening
- Low volume listening — the ES1 brightness becomes more noticeable at low volumes too
- Watching something through the Onkyo where treble harshness is distracting

**The difference is subtle.** Both Direct and Stereo have the sub active and at the same levels. The only practical difference: in Stereo you can use [TONE –] to cut treble −2 dB. If you have done that and the ES1s still sound fine in Direct — stay in Direct, it's marginally cleaner.

---

#### Never use Pure Audio

Pure Audio cuts bass management. The sub receives zero signal. The ES1's four 5-inch woofers have to handle all bass including the frequencies they roll off at — they will distort and the sound will be thin. There is no benefit to Pure Audio in a 2.1 setup with the Yamaha sub.

---

### Step 9 — Set Treble Trim (Stereo mode only)

Only needed if using Stereo mode. Tone controls do not exist in Direct mode.

```
Make sure you are in STEREO mode (press [STEREO] button)
Press [TONE –] repeatedly
```

Each press steps treble down 1 dB. **Start at −2 dB** — this compensates for the ES1's measured +3–6 dB treble peak at 5–20 kHz.

- Still too bright → go to −3 dB
- Sounds dull / lost detail → back to −1 dB
- **Leave Bass at 0 dB** — sub handles bass. Adding EQ bass on the amp creates a double-boost that muddies the crossover region.

> [TONE –] and [TONE +] only work in **Stereo** mode. They are disabled in Direct and Pure Audio.

---

### Step 10 — Set Sub Phase and Fine-Tune Sub Level

Do this last, after everything else is set. Use **Direct mode** throughout this step. Play music with real bass — bass guitar, upright bass, kick drum. Something you know well. Not synth pads or film scores — you need a reference you already know how it should sound.

---

#### Sub Phase — why it matters and how to set it

The phase switch on the Yamaha sub has two positions: **0°** and **180°**. It controls the timing of when the sub's cone moves relative to the ES1 woofers.

When you play a bass note, both the sub and the ES1s reproduce the crossover region (around 80 Hz). If they are in phase, their cones push air at the same moment — the bass adds up and sounds full. If they are out of phase, one cone pushes while the other pulls — they partially cancel each other out. The result sounds like the sub is barely doing anything, or the bass sounds thin and hollow even though the sub is powered on.

**Wrong phase sounds like:** bass is weak even with sub level high, the sub seems inactive, turning the sub off doesn't make much difference.

**Right phase sounds like:** bass is solid, punchy, full — the sub clearly fills in below what the ES1s do.

**Method 1 — SPL meter (most accurate, do this first):**

The sub and mains overlap at 80 Hz (your crossover point). Measure the combined level there — the position that reads higher means they are adding together.

1. Get a tone generator app on your phone (search "Tone Generator" — many free options)
2. Set it to generate **80 Hz sine wave**
3. Play it through the Onkyo at moderate volume in Direct mode (both sub and mains active)
4. Open SPL meter app — set to **C-weighting, Slow**
5. Hold phone at your listening position at ear height
6. Read the SPL with sub phase at **0°** — write it down (e.g. 72 dB)
7. Flip the phase switch to **180°** — read again (e.g. 68 dB)
8. **Use whichever position read higher** — in this example 0° wins

If both positions read the same: the sub's position in the room is exactly equidistant from you and the speakers — either phase works. Leave it at 0°.

**Method 2 — By ear (if no tone generator):**

1. Play a track with steady, repetitive bass — same bass note looping is ideal
2. Switch between 0° and 180° while music plays (you can flip it live)
3. **Use the position where bass sounds louder, fuller, and more physical** — where you feel it more in your chest
4. The wrong position will sound noticeably thinner and smaller

**Most common result:** Sub placed near the front wall between or beside the ES1 towers = **0°** is correct. If you placed the sub behind you or way to the side = **180°** may be better.

---

#### Sub Level — fine-tuning by ear

If you used the SPL meter in Step 6 you already have a calibrated starting point (77–78 dB). Now you verify it sounds right with real music. If you skipped the SPL meter, this is where you set the level entirely by ear.

**Open Level Calibration:**
```
Press [SETUP]
Press [▲][▼]  →  "2. Speaker Setup"  →  [ENTER]
Press [▲][▼]  →  "4. Level Calibration"  →  [ENTER]
Press [▲][▼]  →  navigate to Subwoofer
Press [◄][►]  →  adjust level in 1 dB steps
Press [SETUP]  →  exit when done
```

**What to listen for — three tests:**

**Test 1 — The localisation test (most important)**
Close your eyes and play a track with bass. Point to where the bass seems to come from. You should point at the ES1 towers, not at the Yamaha sub. If you can clearly point to a box in the corner, the sub is too loud. Turn it down 2 dB and test again.

**Test 2 — The on/off test**
Turn the sub off (power switch on the back). Notice the difference — the bottom octave drops away and the ES1s sound thinner. Now turn it back on. The sub should restore the warmth and weight smoothly — it should feel like the speakers just got bigger, not like a separate bass effect was added. If turning the sub on/off feels dramatic and obvious, the sub is too loud.

**Test 3 — Known track test**
Play a recording you know very well — something you've heard on headphones or other good speakers. Bass guitar, acoustic bass, kick drum. Does the weight in the low end match what you know the recording contains? If the bass seems exaggerated compared to what you know the track sounds like, the sub is too hot. If the track sounds thin, the sub needs more.

**Adjustment guide:**
- Sub too loud: bass sounds boomy, one-note, has its own character, you know where it is → reduce 2 dB at a time
- Sub too quiet: music sounds thin, no weight, no physical presence → add 1 dB at a time
- Correct: bass is full and seamless, sounds like it comes from the direction of the ES1s, adding or removing 1 dB makes you feel like something small is missing or overcooked

**Typical result:** If you SPL-calibrated correctly to +2–3 dB, you may need 0–1 dB of adjustment either way. The SPL meter gets you 90% there — the ear gets the last 10%.

---

## You're Done — What to Press Every Day

```
Power on:       [STANDBY/ON]
Select input:   [DVD] for HDMI 1 (Le Potato)
Volume:         [MASTER VOLUME] knob
Listening mode: [LISTENING MODE ►] → DIRECT   (serious music)
                [STEREO] button                (casual / background)
Sub power:      switch on back of Yamaha sub (no auto-on)
```

---

## All Settings at a Glance

```
── Speaker Config ──────────────────────────────
  Subwoofer:    Yes
  Front (ES1):  80 Hz
  Center:       None
  Surround:     None
  Surr Back:    None
  LPF of LFE:   120 Hz
  Double Bass:  Off

── Speaker Distance ────────────────────────────
  Front L/R:    tape-measured to nearest 0.3 m
  Subwoofer:    tape-measured to nearest 0.3 m

── Level Calibration ───────────────────────────
  Front L:      75 dB C-weighted Slow
  Front R:      75 dB C-weighted Slow
  Subwoofer:    77–78 dB (= +2 to +3 dB above mains)

── Audio Adjust ────────────────────────────────
  Dynamic EQ:   Off
  Dynamic Vol:  Off
  Re-EQ:        Off
  Late Night:   Off

── Tone Controls (Stereo mode only) ────────────
  Treble:       −2 dB  (ES1 brightness fix)
  Bass:         0 dB   (never add bass EQ — sub handles it)

── Listening Modes ─────────────────────────────
  Serious music:   Direct
  Casual/BG:       Stereo

── Yamaha Sub ──────────────────────────────────
  Volume knob:     50–60% (calibrated via receiver)
  Crossover knob:  MAX
  Phase:           0° or 180° (whichever reads higher dB at 80 Hz)

── ES1 Placement ───────────────────────────────
  Back wall:       60–90 cm minimum
  Toe-in:          22–30° toward listening seat
```

---

## Listening Modes Reference

### DIRECT — serious / attentive listening

Press **[LISTENING MODE ►]** until display shows `DIRECT`.

What it does:
- Sub active (bass below 80 Hz goes to Yamaha sub) ✓
- No EQ, no tone controls, no loudness compensation — signal is clean
- Distance and level calibration from Step 5/6 still applied ✓
- HDMI video output stays active ✓

Use it for: FLAC/ALAC from MPD, AirPlay 2, Snapcast, any attentive listening session.
Avoid it if: the ES1 tweeter is fatiguing you — switch to Stereo and use [TONE –].

### STEREO — casual / background / Spotify / loud volumes

Press **[STEREO]** button.

What it does:
- Sub active (same as Direct) ✓
- Tone controls enabled → use [TONE –] to set Treble −2 dB
- All other processing (Dynamic EQ, Re-EQ, etc.) stays off because you turned those off in Step 7

Use it for: background music, Spotify, anything where the ES1 brightness is bothering you, high-volume sessions where the tweeter peak is fatiguing.

The sub works identically in both Direct and Stereo. The only functional difference is tone controls.

### PURE AUDIO — never use with this setup

Sub receives zero signal with stereo sources. ES1s play full range and run out of bass extension below 80 Hz. Do not use.

---

## Troubleshooting

### Sub is completely silent

1. Check listening mode — press **[LISTENING MODE ►]** until `DIRECT` (not Pure Audio)
2. Check Speaker Config: `SETUP → 2. Speaker Setup → 2. Speaker Config` → Subwoofer = **Yes**, Front = **80 Hz** (not Full Band)
3. Check RCA cable: plugged into Onkyo **SUBWOOFER PRE OUT** and sub **LINE IN**?
4. Check sub power switch is ON

### Bass is boomy or slow

| Cause | Fix |
|---|---|
| Phase wrong | Flip sub Phase 0° ↔ 180°, pick position that sounds fuller |
| Sub too close to corner | Move sub 10–20 cm away from corner |
| Sub level too high | `SETUP → Speaker Setup → Level Calibration` → lower Subwoofer 2–3 dB |
| Crossover too high | Confirm Front crossover = 80 Hz, not 120 or 150 Hz |

### Treble is harsh or fatiguing

1. Press **[STEREO]** — enables tone controls
2. Press **[TONE –]** twice → Treble = −2 dB
3. If still bright: angle ES1s slightly away from you (reduce toe-in by 5°)

### "NO SIGNAL" on optical input

```
Press [DIGITAL INPUT] → press [◄][►] → select OPT 1 (or OPT 2)
```
Also check:
- TOSLINK cable clicked fully in at both ends (you should feel a click)
- On Le Potato: `amixer sset "AIU SPDIF SRC SEL" I2S`

### Display shows DD or DTS instead of PCM

Le Potato is sending compressed audio. Fix:
```bash
cd ~/music-potato
docker compose restart shairport-sync mpd spotifyd
```

### Sub and mains sound disconnected (two separate sources)

1. Flip sub Phase 0° ↔ 180°
2. Try crossover at 100 Hz instead of 80 Hz
3. Move sub physically closer to the ES1 towers

### Volume low even at 80+

`SETUP → Speaker Setup → Level Calibration` → raise Front L and Front R by +2 to +3 dB.

---

## Sources

- [Fluance ES1 Tower Review + Measurements — Audioholics](https://www.audioholics.com/tower-speaker-reviews/fluance-es1)
- [Fluance ES1 Measurement & Analysis — Audioholics](https://www.audioholics.com/surround-sound-reviews/fluance-es1-surrounds/measurement-and-analysis)
- [Yamaha YST-FSW050 Specs — Yamaha USA](https://usa.yamaha.com/products/audio_visual/speaker_systems/yst-fsw050/specs.html)
- [Subwoofer Calibration & Bass Preferences Guide — AVS Forum](https://www.avsforum.com/threads/guide-to-subwoofer-calibration-and-bass-preferences.2958528/)
- [How to Manually Level Match Speakers — Audioholics](https://www.audioholics.com/frequent-questions/how-to-manually-level-match-speakers)
- [Onkyo TX-SR605 Listening Modes — AVS Forum](https://www.avsforum.com/threads/onkyo-tx-sr605-705-805-listening-modes-explained-purposes-and-benefits.1008717/)
- [Onkyo TX-SR605 Full Manual — ManualsLib](https://www.manualslib.com/manual/302297/Onkyo-Tx-Sr605.html)
- [Subwoofer Crossover Tips — SVS Sound](https://www.svsound.com/blogs/subwoofer-setup-and-tuning/tips-for-setting-the-proper-crossover-frequency-for-a-subwoofer)
- [Speaker Wall Distance Guide — Fluance Support](https://support.fluance.com/s/article/How-far-should-my-speakers-be-from-the-wall)
- [How to Toe-In Speakers Correctly — Totem Acoustic](https://totemacoustic.com/how-to-properly-toe-in-your-speakers-for-optimal-sound/)
