# RoamEN Device Mockup

## Portable Staff Node - Visual Design

### Physical Form Factor

```
┌─────────────────────────────────────┐
│  RoamEN MedComm Badge               │
│  90mm × 60mm × 20mm                 │
│  Weight: 120g                       │
└─────────────────────────────────────┘
```

### Front View (With Display)

```
╔═════════════════════════════════════╗
║  ┌───────────────────────────────┐  ║
║  │    ROAM-42  [WiFi] [BT] [⚡]  │  ║ ← Status bar
║  │                               │  ║
║  │  📢 Emergency Alert            │  ║ ← Alert icon
║  │                               │  ║
║  │  From: A&E Coordinator        │  ║
║  │  Priority: URGENT             │  ║
║  │                               │  ║
║  │  "Major incident - Mass       │  ║
║  │   casualty event. All staff   │  ║ ← Message
║  │   report to stations."        │  ║
║  │                               │  ║
║  │  3 min ago                    │  ║ ← Timestamp
║  └───────────────────────────────┘  ║
║                                     ║
║    🟢 Connected    📶 85%   🔋 67%  ║ ← Indicators
║                                     ║
║   ┌─────┐  ┌─────┐  ┌─────┐        ║
║   │ PTT │  │ ACK │  │ MENU│        ║ ← Buttons
║   └─────┘  └─────┘  └─────┘        ║
║                                     ║
║   [===========] USB-C               ║ ← Charging port
║                                     ║
║   Clip ↓                            ║ ← Belt clip
╚═════════════════════════════════════╝
```

### Screen States

#### 1. Idle Screen
```
┌───────────────────────────────┐
│ ROAM-42  [WiFi] [BT] [⚡]     │
│                               │
│        RoamEN                 │
│      Emergency Comms          │
│                               │
│   🟢 Network OK               │
│   👥 24 nodes online          │
│   📶 Signal: Excellent        │
│                               │
│   Last beacon: 12s ago        │
│                               │
│   [Press PTT to transmit]     │
└───────────────────────────────┘
```

#### 2. Voice Transmission (PTT Pressed)
```
┌───────────────────────────────┐
│ ROAM-42  [WiFi] [BT] [⚡]     │
│                               │
│   🔴 TRANSMITTING...          │
│                               │
│   ▓▓▓▓▓▓▓▓░░░░░░░░           │ ← Audio level
│                               │
│   To: A&E Department          │
│   Mode: Voice (Codec2)        │
│                               │
│   Duration: 00:05             │
│                               │
│   [Hold PTT - Release to end] │
└───────────────────────────────┘
```

#### 3. Receiving Voice
```
┌───────────────────────────────┐
│ ROAM-42  [WiFi] [BT] [⚡]     │
│                               │
│   🔵 RECEIVING                │
│                               │
│   ░░░░░▓▓▓▓▓▓▓▓▓▓▓░░░        │ ← Audio level
│                               │
│   From: Dr. Smith (ICU-05)    │
│   Priority: NORMAL            │
│                               │
│   Duration: 00:03             │
│                               │
│   [Listening...]              │
└───────────────────────────────┘
```

#### 4. Text Message
```
┌───────────────────────────────┐
│ ROAM-42  [WiFi] [BT] [⚡]     │
│                               │
│ 📨 New Message                │
│                               │
│ From: Pharmacy (Node 78)      │
│ Time: 14:23                   │
│                               │
│ "Controlled drugs for bed 12 │
│  ready for collection"        │
│                               │
│ [ACK]  [Reply]  [Delete]      │
└───────────────────────────────┘
```

#### 5. Emergency Alert (Full Screen)
```
┌───────────────────────────────┐
│ 🚨🚨🚨 EMERGENCY 🚨🚨🚨        │
│                               │
│ FIRE ALARM - EAST WING        │
│                               │
│ EVACUATE IMMEDIATELY          │
│                               │
│ ALL STAFF:                    │
│ - Close fire doors            │
│ - Assist patients             │
│ - Muster point: Car Park A    │
│                               │
│ Sent: 14:31 (NOW)             │
│                               │
│ [ACKNOWLEDGE]                 │
└───────────────────────────────┘
```

#### 6. Main Menu
```
┌───────────────────────────────┐
│ ROAM-42  [WiFi] [BT] [⚡]     │
│                               │
│ ┌─────────────────────────┐   │
│ │ > Messages (3 new)      │   │ ← Selected
│ │   Contacts              │   │
│ │   Alerts                │   │
│ │   Settings              │   │
│ │   Network Status        │   │
│ │   Battery & Power       │   │
│ │   About                 │   │
│ └─────────────────────────┘   │
│                               │
│ [▲▼] Navigate  [OK] Select    │
└───────────────────────────────┘
```

#### 7. Network Status
```
┌───────────────────────────────┐
│ Network Status                │
│                               │
│ Status: 🟢 Connected          │
│ Node ID: 42                   │
│ Callsign: ROAM-42             │
│                               │
│ Nodes Online: 24              │
│ ┌─────────────────────────┐   │
│ │ A&E-01    ████ 90% 25m  │   │
│ │ ICU-05    ███░ 73% 48m  │   │
│ │ Base-1    █████ 98% 12m │   │
│ │ Ward-23   ██░░ 45% 120m │   │
│ │ ...more                 │   │
│ └─────────────────────────┘   │
│                               │
│ [Back]              [Refresh] │
└───────────────────────────────┘
```

#### 8. Battery Status
```
┌───────────────────────────────┐
│ Battery & Power               │
│                               │
│  ████████████████░░  67%      │ ← Battery level
│                               │
│ Status: Discharging           │
│ Voltage: 3.82V                │
│ Time Remaining: ~8.2 hours    │
│                               │
│ Usage:                        │
│  RX: 68% ████████░░           │
│  TX: 22% ████░░░░░            │
│  Idle: 10% ██░░░░░░░          │
│                               │
│ [Back]           [Power Save] │
└───────────────────────────────┘
```

---

## Alternative: Phone App Interface

For nodes without built-in display, staff use their phone:

### Phone App - Main Screen
```
╔══════════════════════════════╗
║  🔙  RoamEN     ⚙️  ☰        ║ ← Header
╠══════════════════════════════╣
║                              ║
║  🟢 ROAM-42 Connected        ║
║  📶 Signal: Excellent (95%)  ║
║  🔋 Device: 67% (8h left)    ║
║                              ║
║  ┌────────────────────────┐  ║
║  │  📻 Push to Talk       │  ║ ← Large PTT button
║  │                        │  ║
║  │      [  🎤  ]          │  ║
║  │                        │  ║
║  │  Hold to transmit      │  ║
║  └────────────────────────┘  ║
║                              ║
║  Quick Actions:              ║
║  ┌─────┐ ┌─────┐ ┌─────┐    ║
║  │ 💬  │ │ 🚨  │ │ 📋  │    ║
║  │Msgs │ │Alert│ │Menu │    ║
║  │ (3) │ │     │ │     │    ║
║  └─────┘ └─────┘ └─────┘    ║
║                              ║
║  Recent Activity:            ║
║  ┌────────────────────────┐  ║
║  │ 🔴 Alert 2 min ago     │  ║
║  │ A&E: Mass casualty...  │  ║
║  ├────────────────────────┤  ║
║  │ 💬 Message 15 min ago  │  ║
║  │ Pharmacy: Drugs ready  │  ║
║  ├────────────────────────┤  ║
║  │ 📢 Voice 1h ago        │  ║
║  │ Dr Smith: Patient...   │  ║
║  └────────────────────────┘  ║
║                              ║
╚══════════════════════════════╝
```

### Phone App - Emergency Alert
```
╔══════════════════════════════╗
║    🚨 EMERGENCY ALERT 🚨      ║ ← Red background
╠══════════════════════════════╣
║                              ║
║                              ║
║   FIRE ALARM - EAST WING     ║
║                              ║
║   EVACUATE IMMEDIATELY       ║
║                              ║
║   ALL STAFF:                 ║
║   • Close fire doors         ║
║   • Assist patients          ║
║   • Muster: Car Park A       ║
║                              ║
║   From: Emergency Control    ║
║   Time: 14:31 (NOW)          ║
║                              ║
║  ┌────────────────────────┐  ║
║  │    ACKNOWLEDGE         │  ║ ← Large button
║  └────────────────────────┘  ║
║                              ║
║  Auto-acknowledge in 30s...  ║
║                              ║
╚══════════════════════════════╝
```

---

## LED Indicator Patterns

The device has 3 LEDs on the front:

### Green LED (Network Status)
- **Solid**: Connected to network
- **Slow blink**: Searching for network
- **Fast blink**: Transmitting
- **Off**: No power / offline

### Red LED (Alert Status)
- **Off**: Normal operation
- **Slow blink**: Unread message
- **Fast blink**: Urgent alert
- **Solid**: Emergency alert

### Blue LED (Activity)
- **Off**: Idle
- **Blink**: Receiving data
- **Solid**: Voice RX in progress

---

## Audio Feedback

### Alert Tones (Played through speaker)

**Standard Alert** (Low priority):
```
♪ beep-beep ♪  (800Hz → 1000Hz, 300ms each)
```

**Urgent Alert** (Medium priority):
```
♪ wee-woo-wee-woo-wee ♪  (800Hz ↔ 1200Hz alternating, 200ms each)
```

**Emergency Alert** (Critical):
```
♪ WEE-WOO-WEE-WOO-WEE-WOO ♪  (600Hz ↔ 1200Hz rapid, 150ms each)
LOUD, INSISTENT, IMPOSSIBLE TO IGNORE
```

### Voice Quality

**Codec2 @ 700 bps**:
- Intelligible but robotic
- Like old walkie-talkies
- Perfectly understandable for emergencies
- "Patient in bed 3 needs assistance" → Clear
- Not suitable for music, but perfect for speech

---

## User Workflows

### 1. Sending a Voice Message

```
Staff member workflow:
┌─────────────────┐
│ 1. Press PTT    │ → Device beeps once
│    button       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Speak        │ → Screen shows "TRANSMITTING"
│    message      │    Red LED blinks
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Release PTT  │ → Device beeps twice
│                 │    Message sent
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Confirmation │ → "Message delivered to 12 nodes"
└─────────────────┘
```

### 2. Receiving an Emergency Alert

```
Automatic workflow:
┌──────────────────┐
│ Emergency sent   │ → From coordinator
│ (0xFF broadcast) │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Alert tone plays │ → 🚨 WEE-WOO-WEE-WOO 🚨
│ (emergency.wav)  │    LOUD
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Screen shows     │ → Full screen takeover
│ alert (red)      │    Red LED solid
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ User reads &     │ → Press ACK button
│ acknowledges     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ ACK sent back    │ → Coordinator knows staff saw it
│ to sender        │
└──────────────────┘
```

### 3. Checking Network Status

```
Quick check workflow:
┌──────────────────┐
│ Glance at device │ → LEDs show status at a glance
└────────┬─────────┘
         │
  Green LED on?  ───Yes──→ Connected ✅
         │
         No
         │
         ▼
┌──────────────────┐
│ Press MENU       │ → Navigate to "Network Status"
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ View detailed    │ → See all nodes, signal strength
│ network info     │    Last beacon time, hop count
└──────────────────┘
```

---

## Size Comparison

```
┌────────────────┐
│                │
│   iPhone 14    │ ← Reference
│   (146mm tall) │
│                │
│                │
└────────────────┘

┌──────────┐
│          │
│ RoamEN   │ ← 90mm tall (62% of iPhone height)
│ Device   │
│          │
└──────────┘

     ┌──┐
     │CC│    ← Credit card (85mm × 54mm) for reference
     └──┘
```

**Fits in**:
- Large pocket (with slight bulge)
- Lanyard around neck
- Belt clip
- Tactical vest pocket
- Scrubs pocket (may be tight)

---

## Mounting Options

### 1. Lanyard (Most Common)
```
    ╱╲
   ╱  ╲
  │    │  ← Lanyard loop
  │    │
  ├────┤
  │Dev │  ← Device hangs at chest level
  │ice │     Easy to see/access
  └────┘
```

### 2. Belt Clip
```
  ┌─────┐
  │Dev  │  ← Device on belt
  │ice  │     Secure, out of way
  └──┬──┘
     │
   ═╪═══  ← Belt
     │
```

### 3. Tactical Vest / Scrubs Pocket
```
┌─────────┐
│  VEST   │
│ ┌─────┐ │  ← Device in pocket
│ │ Dev │ │     Quick access
│ │ ice │ │     Protected
│ └─────┘ │
└─────────┘
```

---

## Usage Scenarios

### Scenario 1: Normal Day
- Device clipped to belt
- Green LED solid (connected)
- Occasional beep (text message from pharmacy)
- Staff glances at screen, reads message
- Presses ACK button
- Goes about their day

### Scenario 2: Major Incident
- Emergency alert broadcast
- **LOUD siren plays** (emergency.wav)
- Screen shows: "MAJOR INCIDENT - MASS CASUALTY"
- Staff member:
  1. Acknowledges alert
  2. Reads instructions
  3. Presses PTT: "ICU ready to receive 4 critical"
  4. Hears responses from A&E coordinator
  5. Coordinates patient transfers via voice

### Scenario 3: IT Failure
- Hospital WiFi down
- PABX phones offline
- Mobile network congested
- **RoamEN still works** (independent)
- Staff can still communicate
- Beacons every 30s confirm network alive
- Business continues

---

## Future Enhancements

### Version 2 Hardware
- Smaller (phone-sized)
- Touchscreen instead of buttons
- GPS integration
- Longer battery (20+ hours)
- Better speaker (louder)
- Vibration alerts
- Color display

### Version 2 Software
- Group voice calls
- Location tracking on map
- Patient handoff protocols
- Integration with EPR
- Automatic incident logging
- AI-assisted triage

---

**Document Version**: 1.0
**Last Updated**: 2025-11-19
**Status**: Mockup (not yet implemented)
