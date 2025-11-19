# RoamEN Development Setup Guide

## Overview

This guide covers setting up a RoamEN development environment from scratch, whether you're developing on macOS, Linux, or Raspberry Pi.

---

## Quick Start (5 Minutes)

```bash
# Clone the repository
git clone https://github.com/mb43/roamen.git
cd roamen

# Install Python dependencies
pip3 install -r firmware/node/requirements.txt

# Run the tests
cd firmware/node
python3 test_roamen.py

# You should see: 🎉 ALL TESTS PASSED!
```

---

## Development Environments

### Option 1: macOS (Recommended for Development)

**Advantages**:
- Fast iteration
- Full GUI tools available
- Same Python code runs on Pi
- Can simulate radio (GNU Radio)

**Setup Time**: 15 minutes

#### Prerequisites

```bash
# Install Xcode Command Line Tools
xcode-select --install

# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python@3.11

# Install audio dependencies
brew install portaudio
```

#### Clone and Setup

```bash
# Create project directory
mkdir ~/Projects
cd ~/Projects

# Clone repository
git clone https://github.com/mb43/roamen.git
cd roamen

# Install Python dependencies
pip3 install -r firmware/node/requirements.txt

# Verify installation
cd firmware/node
python3 test_roamen.py
```

#### Expected Output

```
============================================================
🚀 RoamEN Protocol Test Suite
============================================================

🧪 Testing basic packet creation...
  ✅ Packed: 39 bytes
🧪 Testing packet unpacking...
  ✅ RoamENPacket(type=BEACON, src=1, dst=65535, pri=INFO, payload=7B)
🧪 Testing alert packet...
  ✅ Emergency alert: 'MAYDAY MAYDAY - Fire at TQ123456'
  ✅ Priority: EMERGENCY
🧪 Testing checksum validation...
⚠️  Checksum mismatch: expected 58463, got 26722
  ✅ Corruption detected correctly
🧪 Testing broadcast vs unicast...
  ✅ Addressing works

============================================================
🎉 ALL TESTS PASSED! Protocol is WORKING!
============================================================
```

#### Optional: GNU Radio (for SDR development)

```bash
# Install GNU Radio
brew install gnuradio

# Install additional blocks
pip3 install gnuradio

# Verify
gnuradio-config-info --version
```

### Option 2: Linux (Ubuntu/Debian)

**Advantages**:
- Native environment (same as Raspberry Pi OS)
- All tools available
- Good for testing

**Setup Time**: 10 minutes

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y \
    python3 python3-pip \
    git \
    libportaudio2 libportaudiocpp0 portaudio19-dev \
    python3-numpy python3-scipy \
    gnuradio

# Clone repository
git clone https://github.com/mb43/roamen.git
cd roamen

# Install Python packages
pip3 install -r firmware/node/requirements.txt

# Run tests
cd firmware/node
python3 test_roamen.py
```

### Option 3: Raspberry Pi (Target Platform)

**Advantages**:
- Real hardware
- Actual performance testing
- Hardware GPIO access

**Setup Time**: 30 minutes

#### Flash Raspberry Pi OS

```bash
# On your computer:
# 1. Download Raspberry Pi Imager
#    https://www.raspberrypi.com/software/

# 2. Flash "Raspberry Pi OS (64-bit)" to SD card
# 3. Enable SSH in imager settings
# 4. Set hostname: roamen-node-01
# 5. Set WiFi credentials
# 6. Insert SD card and boot Pi
```

#### Initial Pi Setup

```bash
# SSH into Pi
ssh pi@roamen-node-01.local

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y \
    python3 python3-pip git \
    libportaudio2 portaudio19-dev \
    python3-numpy python3-scipy python3-yaml \
    gnuradio gr-osmosdr

# Clone repository
git clone https://github.com/mb43/roamen.git
cd roamen

# Install Python packages
pip3 install -r firmware/node/requirements.txt

# Run tests
cd firmware/node
python3 test_roamen.py
```

---

## Project Structure

```
roamen/
├── README.md                      # Project overview
├── LICENSE                        # GPL-3.0
├── .gitignore                     # Git ignore rules
│
├── firmware/                      # Node software
│   └── node/
│       ├── protocol/              # Protocol implementation
│       │   ├── __init__.py
│       │   └── packet.py          # Packet encode/decode
│       ├── radio/                 # Radio interface (Phase 2)
│       ├── audio/                 # Audio processing (Phase 2)
│       ├── web/                   # Web UI (Phase 2)
│       ├── config/                # Configuration files
│       │   └── node_config.yaml   # Node settings
│       ├── requirements.txt       # Python dependencies
│       ├── test_roamen.py         # Test suite
│       └── generate_alert_tones.py # Alert tone generator
│
├── ui/                            # User interface
│   ├── web/                       # Web-based UI (Phase 2)
│   └── assets/
│       └── alert_tones/           # Generated WAV files
│           ├── standard.wav
│           ├── urgent.wav
│           └── emergency.wav
│
├── docs/                          # Documentation
│   ├── ARCHITECTURE.md            # System architecture
│   ├── business_case/             # Hospital deployment
│   │   └── HOSPITAL_DEPLOYMENT.md
│   ├── technical/                 # Technical specs
│   │   └── PROTOCOL_SPEC.md
│   ├── guides/                    # Setup guides
│   │   └── DEVELOPMENT_SETUP.md   # This file
│   └── hardware/                  # Hardware specs
│       └── SPECIFICATIONS.md
│
└── tests/                         # Additional tests (future)
```

---

## Development Workflow

### 1. Generate Alert Tones

```bash
cd firmware/node
python3 generate_alert_tones.py
```

**Output**:
```
🎵 Generating RoamEN Alert Tones...

✅ Generated: ../../ui/assets/alert_tones/standard.wav
✅ Generated: ../../ui/assets/alert_tones/urgent.wav
✅ Generated: ../../ui/assets/alert_tones/emergency.wav

🎉 All alert tones generated!
```

**Test tones** (macOS):
```bash
afplay ../../ui/assets/alert_tones/standard.wav
afplay ../../ui/assets/alert_tones/urgent.wav
afplay ../../ui/assets/alert_tones/emergency.wav
```

**Test tones** (Linux/Pi):
```bash
aplay ../../ui/assets/alert_tones/standard.wav
aplay ../../ui/assets/alert_tones/urgent.wav
aplay ../../ui/assets/alert_tones/emergency.wav
```

### 2. Run Tests

```bash
cd firmware/node
python3 test_roamen.py
```

All tests should pass ✅

### 3. Make Changes

Edit protocol code:
```bash
# Edit the packet implementation
nano protocol/packet.py

# Or use your favorite editor
code protocol/packet.py  # VS Code
vim protocol/packet.py   # Vim
```

### 4. Test Changes

```bash
python3 test_roamen.py
```

Always run tests after changes!

### 5. Commit Changes

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## Common Development Tasks

### Adding a New Packet Type

**Example**: Adding a `STATUS` packet

1. **Edit `protocol/packet.py`**:

```python
class PacketType(IntEnum):
    """RoamEN packet types"""
    BEACON = 0x01
    TEXT_MESSAGE = 0x02
    VOICE_START = 0x03
    VOICE_DATA = 0x04
    VOICE_END = 0x05
    ALERT = 0x06
    ACK = 0x07
    FILE_CHUNK = 0x10
    STATUS = 0x08  # NEW: Status update packet
    EMERGENCY_BROADCAST = 0xFF
```

2. **Add helper class** (optional):

```python
class StatusPacket:
    """Helper for creating and parsing status packets"""

    @staticmethod
    def create(source_id: int, dest_id: int, status_message: str) -> RoamENPacket:
        """Create a status packet"""
        payload = status_message.encode('utf-8')[:128]

        return RoamENPacket(
            packet_type=PacketType.STATUS,
            source_id=source_id,
            dest_id=dest_id,
            priority=Priority.INFO,
            payload=payload
        )

    @staticmethod
    def parse(packet: RoamENPacket) -> Optional[str]:
        """Parse status packet payload"""
        if packet.packet_type != PacketType.STATUS:
            return None

        return packet.payload.decode('utf-8').rstrip('\x00')
```

3. **Add tests** in `test_roamen.py`:

```python
def test_status():
    print("🧪 Testing status packet...")

    status = StatusPacket.create(1, 0xFFFF, "Node operational")
    data = status.pack()

    status_rx = RoamENPacket.unpack(data)
    assert status_rx is not None

    message = StatusPacket.parse(status_rx)
    assert "operational" in message

    print(f"  ✅ Status: '{message}'")
```

4. **Run tests**:

```bash
python3 test_roamen.py
```

### Modifying Configuration

Edit `config/node_config.yaml`:

```yaml
node:
  id: 1                      # Unique node ID (1-65534)
  callsign: "ROAM-01"        # Node callsign (16 chars max)
  role: "coordinator"        # Role: coordinator, relay, client

radio:
  frequency: 433500000       # 433.5 MHz
  mode: "freedv_700d"        # FreeDV mode
  tx_power: 10               # TX power in dBm (max 10)

audio:
  input_device: "default"    # Microphone
  output_device: "default"   # Speaker
  sample_rate: 8000          # 8kHz (Codec2)

network:
  beacon_interval: 30        # Beacon every 30 seconds
  buddy_timeout: 300         # 5 minutes offline = timeout
```

Load config in Python:

```python
import yaml

with open('config/node_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

node_id = config['node']['id']
frequency = config['radio']['frequency']
```

---

## Hardware Setup

### Connecting RTL-SDR (Reception Testing)

```bash
# Linux/Pi: Install drivers
sudo apt install rtl-sdr

# Plug in RTL-SDR USB dongle

# Test reception
rtl_test -t

# Expected output:
# Found 1 device(s):
#   0:  Realtek, RTL2838UHIDIR, SN: 00000001
```

**Scan 433MHz band**:
```bash
rtl_power -f 433M:434M:10k -g 50 -i 1 433mhz_scan.csv
```

### Connecting HackRF (Transmission Testing)

```bash
# Linux/Pi: Install tools
sudo apt install hackrf

# Plug in HackRF USB

# Test
hackrf_info

# Expected output:
# Found HackRF
# Serial number: 0x...
# Firmware version: ...
```

**Transmit test tone** (BE CAREFUL):
```bash
# Generate test tone (1kHz)
hackrf_transfer -t test_tone.wav -f 433500000 -s 8000000 -a 1
```

---

## Testing Strategy

### Unit Tests

Test individual functions:

```python
def test_crc16():
    """Test CRC16 calculation"""
    data = b"ROAM test data"
    crc = RoamENPacket._crc16(data)
    assert isinstance(crc, int)
    assert 0 <= crc <= 0xFFFF
```

Run with:
```bash
python3 test_roamen.py
```

### Integration Tests

Test multiple components together:

```python
def test_packet_round_trip():
    """Test packet encode/decode"""
    # Create packet
    p1 = RoamENPacket(PacketType.TEXT_MESSAGE, 1, 42, payload=b"Test")

    # Encode
    data = p1.pack()

    # Decode
    p2 = RoamENPacket.unpack(data)

    # Verify
    assert p1.packet_type == p2.packet_type
    assert p1.source_id == p2.source_id
    assert p1.dest_id == p2.dest_id
    assert p1.payload == p2.payload
```

### Over-the-Air Tests

Test with actual radio hardware:

```bash
# Terminal 1 (RX node)
python3 roamen_node.py --config config/node_rx.yaml

# Terminal 2 (TX node)
python3 roamen_node.py --config config/node_tx.yaml --send "Test message"
```

---

## Debugging

### Enable Debug Logging

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.debug("Debug message")
```

### Inspect Packets

```python
# Create packet
p = RoamENPacket(PacketType.BEACON, 1, 0xFFFF, payload=b"ROAM-01")
data = p.pack()

# Inspect raw bytes
print("Raw packet:", data.hex())
print("Length:", len(data))

# Parse header
sync = data[0:4]
version = data[4]
packet_type = data[5]
print(f"SYNC: {sync}, VERSION: {version:02x}, TYPE: {packet_type:02x}")
```

### Monitor RF

**Spectrum analyzer** (GUI):
```bash
gqrx
# Tune to 433.5 MHz
# Watch waterfall for signals
```

**Command line**:
```bash
rtl_power -f 433M:434M:10k -g 50 -i 1 scan.csv
# Analyze scan.csv for activity
```

---

## Performance Testing

### Packet Throughput

```python
import time

# Send 1000 packets
start = time.time()
for i in range(1000):
    p = RoamENPacket(PacketType.TEXT_MESSAGE, 1, 42, payload=f"Message {i}".encode())
    data = p.pack()
    # transmit(data)

end = time.time()
duration = end - start
pps = 1000 / duration  # Packets per second

print(f"Throughput: {pps:.1f} packets/second")
```

### Memory Usage

```python
import sys

p = RoamENPacket(PacketType.BEACON, 1, 0xFFFF, payload=b"ROAM-01")
data = p.pack()

print(f"Packet object size: {sys.getsizeof(p)} bytes")
print(f"Packed data size: {len(data)} bytes")
```

### Battery Life Estimation

```python
# Assume 2000mAh battery, 3.7V

# Power consumption (measured)
idle_current_ma = 150  # mA
tx_current_ma = 400    # mA
rx_current_ma = 200    # mA

# Usage pattern (percentage of time)
idle_time_pct = 0.10
tx_time_pct = 0.20
rx_time_pct = 0.70

# Weighted average current
avg_current_ma = (
    idle_current_ma * idle_time_pct +
    tx_current_ma * tx_time_pct +
    rx_current_ma * rx_time_pct
)

# Battery life
battery_capacity_mah = 2000
battery_life_hours = battery_capacity_mah / avg_current_ma

print(f"Average current: {avg_current_ma:.1f} mA")
print(f"Estimated battery life: {battery_life_hours:.1f} hours")
```

---

## Continuous Integration

### GitHub Actions (Planned)

Create `.github/workflows/test.yml`:

```yaml
name: RoamEN Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y libportaudio2 portaudio19-dev
        pip install -r firmware/node/requirements.txt

    - name: Run tests
      run: |
        cd firmware/node
        python3 test_roamen.py
```

---

## Troubleshooting

### Problem: Tests fail with import errors

**Solution**:
```bash
# Ensure you're in the right directory
cd firmware/node

# Check Python path
python3 -c "import sys; print(sys.path)"

# Install dependencies
pip3 install -r requirements.txt
```

### Problem: Audio playback doesn't work

**macOS**:
```bash
# Check audio devices
system_profiler SPAudioDataType

# Use afplay (built-in)
afplay ui/assets/alert_tones/standard.wav
```

**Linux/Pi**:
```bash
# Install ALSA utils
sudo apt install alsa-utils

# List devices
aplay -l

# Test playback
aplay ui/assets/alert_tones/standard.wav
```

### Problem: RTL-SDR not detected

```bash
# Check USB connection
lsusb | grep Realtek

# Check driver
rtl_test -t

# If not found, reinstall driver
sudo apt install --reinstall rtl-sdr
```

### Problem: Permission denied on USB devices

```bash
# Add user to dialout group (Linux/Pi)
sudo usermod -a -G dialout $USER

# Logout and login again
```

---

## Next Steps

After completing setup:

1. **Explore the code**: Read through `protocol/packet.py`
2. **Run all tests**: Verify everything works
3. **Generate tones**: Create alert sound files
4. **Read documentation**: Study `docs/ARCHITECTURE.md` and `docs/technical/PROTOCOL_SPEC.md`
5. **Get hardware**: Order RTL-SDR and HackRF (see `docs/hardware/SPECIFICATIONS.md`)
6. **Join development**: Contribute to the project!

---

## Getting Help

**Documentation**:
- Architecture: `docs/ARCHITECTURE.md`
- Protocol: `docs/technical/PROTOCOL_SPEC.md`
- Hardware: `docs/hardware/SPECIFICATIONS.md`

**Issues**:
- GitHub Issues: https://github.com/mb43/roamen/issues

**Community**:
- (Future: Discord/Slack channel)

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes
4. Run tests: `python3 test_roamen.py`
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature/my-feature`
7. Create Pull Request

**Code Style**:
- PEP 8 for Python
- Type hints preferred
- Docstrings for public functions
- Tests for new features

---

**Document Version**: 1.0
**Last Updated**: 2025-11-19
**Status**: Phase 1 - MVP
