# RoamEN System Architecture

## Overview

RoamEN (Roaming Emergency Network) is an independent emergency communication system designed for healthcare facilities and emergency response scenarios where traditional communication infrastructure may fail.

## System Components

### 1. Network Layer

#### Protocol Stack
```
┌─────────────────────────────────────┐
│   Application Layer                 │
│   (Voice, Text, Alerts)             │
├─────────────────────────────────────┤
│   Transport Layer                   │
│   (RoamEN Protocol)                 │
├─────────────────────────────────────┤
│   Physical Layer                    │
│   (FreeDV/Codec2 over 433MHz)       │
└─────────────────────────────────────┘
```

#### RoamEN Protocol
- **Header Size**: 32 bytes
- **Max Payload**: Configurable (default 256 bytes)
- **Error Detection**: CRC16-CCITT
- **Addressing**: 16-bit node IDs (1-65534)
- **Broadcast**: 0xFFFF
- **TTL**: Hop-based (default 5)

### 2. Hardware Architecture

#### Node Types

**Fixed Infrastructure Nodes** (HackRF-based)
- Always-on mesh backbone
- Mains powered
- High-gain antennas
- Relay and routing functions
- Coverage: ~1-3km urban, ~5km rural

**Portable Staff Nodes** (Pi Zero 2W-based)
- Battery powered (12+ hours)
- Clip-on/lanyard mount
- TX/RX capable
- Voice + text + alerts
- Coverage: Direct or via relay

#### Reference Hardware

**Development (Phase 1)**
- Raspberry Pi 4 (4GB)
- HackRF One (TX/RX)
- RTL-SDR Blog V3 (RX)
- 433MHz antenna
- USB sound card

**Production (Phase 3)**
- Raspberry Pi Zero 2W
- RFM69HCW 433MHz transceiver
- 2000mAh LiPo battery
- 0.96" OLED display (optional)
- Bluetooth (phone interface)

### 3. Software Architecture

```
roamen/
├── firmware/
│   └── node/
│       ├── protocol/          # Core protocol implementation
│       │   ├── packet.py      # Packet encode/decode
│       │   └── __init__.py
│       ├── radio/             # Radio interface (Phase 2)
│       ├── audio/             # Audio processing (Phase 2)
│       ├── web/               # Web UI (Phase 2)
│       ├── config/            # Configuration
│       └── generate_alert_tones.py
├── ui/                        # User interface
│   ├── web/                   # Web-based UI
│   └── assets/                # Alert tones, icons
├── docs/                      # Documentation
│   ├── business_case/         # Hospital deployment docs
│   ├── technical/             # Technical specifications
│   ├── guides/                # Setup and user guides
│   └── hardware/              # Hardware specifications
└── tests/                     # Test suite
```

## Packet Structure

### Header Format (32 bytes)
```
Offset | Size | Field       | Description
-------|------|-------------|----------------------------------
0      | 4    | SYNC        | Magic bytes: 'ROAM'
4      | 1    | VERSION     | Protocol version (0x01)
5      | 1    | TYPE        | Packet type
6      | 2    | SOURCE_ID   | Source node ID
8      | 2    | DEST_ID     | Destination ID (0xFFFF = broadcast)
10     | 1    | PRIORITY    | Priority level (0-9)
11     | 1    | TTL         | Time to live (hops)
12     | 4    | TIMESTAMP   | Unix timestamp
16     | 2    | PAYLOAD_LEN | Payload length
18     | 2    | CHECKSUM    | CRC16-CCITT
20     | 12   | RESERVED    | Reserved for future use
```

### Packet Types
| Type | Value | Description |
|------|-------|-------------|
| BEACON | 0x01 | Network presence |
| TEXT_MESSAGE | 0x02 | Chat message |
| VOICE_START | 0x03 | Voice transmission start |
| VOICE_DATA | 0x04 | Voice data chunk |
| VOICE_END | 0x05 | Voice transmission end |
| ALERT | 0x06 | Selective call/alert |
| ACK | 0x07 | Acknowledgement |
| FILE_CHUNK | 0x10 | File transfer chunk |
| EMERGENCY_BROADCAST | 0xFF | Emergency override |

### Priority Levels
| Priority | Value | Usage |
|----------|-------|-------|
| INFO | 0 | Beacons, status updates |
| NORMAL | 1 | Regular messages |
| URGENT | 2 | Important alerts |
| EMERGENCY | 9 | Life-threatening emergencies |

## Network Topology

### Mesh Network Design
```
[Fixed Node 1]───[Fixed Node 2]───[Fixed Node 3]
      │    ╲         │         ╱       │
      │     ╲        │        ╱        │
      │      ╲       │       ╱         │
[Fixed Node 4]───[Fixed Node 5]───[Fixed Node 6]
      │              │              │
      │              │              │
   [Staff]        [Staff]        [Staff]
   Nodes          Nodes          Nodes
```

### Hospital Deployment Model
- **Infrastructure**: 20-50 fixed HackRF nodes
- **Coverage**: All floors, all departments
- **Portable**: 5,000 staff nodes
- **Redundancy**: Multiple paths between nodes
- **Failover**: Automatic re-routing

## Security Considerations

### Current Status (Phase 1)
- ❌ No encryption (plaintext)
- ✅ CRC16 integrity checking
- ✅ Node ID validation
- ⚠️ Suitable for proof of concept only

### Planned (Phase 2)
- ✅ AES-256 encryption
- ✅ Message authentication codes
- ✅ Key distribution protocol
- ✅ Perfect forward secrecy

### Medical Device Compliance
- Must meet medical device regulations
- Patient data protection
- HIPAA/GDPR compliance required
- Audit logging

## Performance Specifications

### Target Metrics
- **Latency**: <500ms end-to-end
- **Voice Quality**: Intelligible (Codec2)
- **Range**: 1-3km urban, 5km rural
- **Battery Life**: 12+ hours continuous
- **Reliability**: 99.5% uptime
- **Capacity**: 5,000 simultaneous users

### Voice Codec
- **Codec**: Codec2 (FreeDV)
- **Mode**: 700D (700 bits/s)
- **Quality**: Intelligible, not HiFi
- **Latency**: ~40ms encode/decode
- **Bandwidth**: 700 bps + overhead

## Deployment Phases

### Phase 1: Proof of Concept (Months 1-3)
- ✅ Protocol implementation
- ✅ Basic packet TX/RX
- ✅ Alert tones
- ⏳ FreeDV integration
- ⏳ 2-node communication test

### Phase 2: Development (Months 4-6)
- Custom hardware design
- PCB layout
- Prototype manufacturing
- Software refinement
- Integration testing

### Phase 3: Pilot (Months 7-9)
- 100 nodes in A&E department
- Real-world testing
- User feedback
- Performance measurement
- Iteration

### Phase 4: Production (Months 10-18)
- 5,000 node manufacturing
- Infrastructure installation
- Phased department rollout
- Training program
- Full deployment

## Integration Points

### Hospital Systems
- **Paging System**: One-way integration (receive pages)
- **WiFi Network**: Fallback/bridging when available
- **PABX**: Phone system integration
- **Fire Alarm**: Automatic emergency broadcasts
- **Building Management**: Integration with facilities

### External Systems
- **Emergency Services**: 999 call integration
- **NHS Systems**: EPR/patient records (future)
- **National Infrastructure**: NHS emergency network (future)

## Scalability

### Small Deployment (10-50 users)
- 2-3 fixed infrastructure nodes
- Point-to-point or simple mesh
- Cost: £5K-15K

### Medium Deployment (50-500 users)
- 5-10 infrastructure nodes
- Mesh network
- Cost: £15K-50K

### Large Deployment (500-5000 users)
- 20-50 infrastructure nodes
- Full mesh with redundancy
- Cost: £200K-500K

## Technology Stack

### Languages
- **Python 3.10+**: Main application logic
- **C/C++**: FreeDV/Codec2 (existing libraries)
- **JavaScript**: Web UI (future)

### Key Libraries
- **pyserial**: Radio interface
- **numpy/scipy**: Signal processing
- **aiohttp**: Web server
- **websockets**: Real-time UI updates
- **pyyaml**: Configuration

### Hardware Interfaces
- **GNU Radio**: SDR processing
- **FreeDV**: Digital voice
- **RFM69**: Radio transceiver
- **I2C/SPI**: Display/peripherals

## Standards Compliance

### Regulatory
- **UK**: IR 2030 (433MHz ISM band, 10mW ERP)
- **EU**: ETSI EN 300 220
- **Medical**: Future certification required

### Technical
- **Protocol**: Custom (RoamEN)
- **Voice**: Codec2 (open standard)
- **Encryption**: AES-256 (NIST FIPS 140-2)

## Future Enhancements

### Short Term (6 months)
- Encryption implementation
- Web UI development
- Mobile app (iOS/Android)
- GPS integration
- Message persistence

### Medium Term (12 months)
- Advanced mesh routing
- Quality of Service (QoS)
- Multi-channel operation
- Automatic frequency selection
- Network diagnostics

### Long Term (24+ months)
- Satellite uplink
- Long-range mode (LoRa)
- AI-assisted triage
- Video capability (low quality)
- National network integration

## References

- **Codec2**: http://www.rowetel.com/codec2.html
- **FreeDV**: https://freedv.org/
- **HackRF**: https://greatscottgadgets.com/hackrf/
- **RFM69**: https://www.hoperf.com/modules/rf_transceiver/RFM69HCW.html

---

**Document Version**: 1.0
**Last Updated**: 2025-11-19
**Status**: Phase 1 - MVP Development
