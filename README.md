# RoamEN - Roaming Emergency Network

**Emergency SDR communication system with digital voice and selective alerting**

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![Status](https://img.shields.io/badge/status-Phase%201%20MVP-orange.svg)]()

## Overview

RoamEN is an independent emergency communication system designed for healthcare facilities and emergency response scenarios where traditional infrastructure fails. When IT systems, power, or cellular networks are down, RoamEN provides reliable voice, text, and alert communication.

**Key Features**:
- 🔊 Digital voice (Codec2/FreeDV)
- 💬 Text messaging
- 🚨 Priority-based alerts (Standard, Urgent, Emergency)
- 🔋 Battery powered (12+ hours)
- 📡 Mesh networking
- 🔓 Open source (GPL-3.0)
- 💰 Affordable (£102/user vs £455-£1,003 for alternatives)

## Status: Phase 1 - MVP Development

✅ **Completed**:
- Protocol implementation (32-byte header, CRC16)
- Packet types (beacon, text, voice, alerts)
- Alert tone generation
- Test suite (100% passing)
- Comprehensive documentation

🚧 **In Progress**:
- FreeDV integration
- Radio interface
- Web UI

📋 **Planned**:
- Custom hardware design
- Hospital pilot deployment
- Encryption and security

## Quick Start

```bash
# Clone repository
git clone https://github.com/mb43/roamen.git
cd roamen

# Install dependencies
pip3 install -r firmware/node/requirements.txt

# Run tests
cd firmware/node
python3 test_roamen.py

# Generate alert tones
python3 generate_alert_tones.py

# Test tones (macOS)
afplay ../../ui/assets/alert_tones/emergency.wav
```

See [Development Setup Guide](docs/guides/DEVELOPMENT_SETUP.md) for detailed instructions.

## Use Case: Hospital Deployment

RoamEN is being developed for deployment in a 15,000-staff hospital with 5,000 on-duty at any time:

- **Infrastructure**: 50 fixed relay nodes
- **Portable**: 5,000 staff nodes
- **Investment**: £508K over 24 months
- **Cost per user**: £102
- **Benefits**: 40-50% cheaper than alternatives, works when everything else fails

See [Hospital Deployment Business Case](docs/business_case/HOSPITAL_DEPLOYMENT.md) for details.

## Hardware Requirements

### Development (Phase 1 - Current)
- Raspberry Pi 4 (4GB)
- HackRF One (TX/RX)
- RTL-SDR Blog V3 (RX)
- 433MHz antennas
- USB sound card

**Cost**: ~£350 per node

### Production (Phase 3 - Target)
- Raspberry Pi Zero 2W
- RFM69HCW 433MHz transceiver
- 2000mAh LiPo battery
- OLED display or phone app

**Cost**: ~£75 per node (volume)

See [Hardware Specifications](docs/hardware/SPECIFICATIONS.md) for details.

## Architecture

```
┌─────────────────────────────────────┐
│   Application Layer                 │
│   (Voice, Text, Alerts)             │
├─────────────────────────────────────┤
│   RoamEN Protocol                   │
│   (32-byte header, CRC16)           │
├─────────────────────────────────────┤
│   Physical Layer                    │
│   (FreeDV/Codec2 @ 433MHz)          │
└─────────────────────────────────────┘
```

- **Protocol**: Custom binary format, 32-byte header
- **Error Detection**: CRC16-CCITT
- **Addressing**: 16-bit node IDs, broadcast support
- **Priority**: 4 levels (INFO, NORMAL, URGENT, EMERGENCY)
- **Voice**: Codec2 (700 bps, intelligible quality)
- **Range**: 1-3km urban, 5km rural

See [Architecture Documentation](docs/ARCHITECTURE.md) for full details.

## Documentation

### Getting Started
- [Development Setup Guide](docs/guides/DEVELOPMENT_SETUP.md) - Set up your development environment
- [Quick Start](#quick-start) - Get running in 5 minutes

### Technical
- [Architecture](docs/ARCHITECTURE.md) - System design and components
- [Protocol Specification](docs/technical/PROTOCOL_SPEC.md) - Packet format and behavior
- [Hardware Specifications](docs/hardware/SPECIFICATIONS.md) - Component requirements

### Business
- [Hospital Deployment](docs/business_case/HOSPITAL_DEPLOYMENT.md) - £508K business case for NHS

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

**Areas needing help**:
- FreeDV integration
- Mesh routing algorithms
- Web UI development
- Testing and documentation
- Hardware design

## License

GPL-3.0 - see [LICENSE](LICENSE) for details.

This means:
- ✅ Free to use, modify, distribute
- ✅ Commercial use allowed
- ✅ NHS Trusts can customize freely
- ⚠️ Modifications must be shared (copyleft)

## Project Status

| Phase | Status | Timeline | Investment |
|-------|--------|----------|------------|
| 1. Proof of Concept | ✅ In Progress | Months 1-3 | £1,000 |
| 2. Development | 📋 Planned | Months 4-6 | £10,000 |
| 3. Pilot (A&E) | 📋 Planned | Months 7-9 | £15,000 |
| 4. Refinement | 📋 Planned | Months 10-12 | £10,000 |
| 5. Manufacturing | 📋 Planned | Months 13-15 | £400,000 |
| 6. Deployment | 📋 Planned | Months 16-21 | £50,000 |
| 7. Handover | 📋 Planned | Months 22-24 | £22,350 |

**Total**: £508,350 over 24 months for 5,000-user deployment

## Contact

- **Issues**: [GitHub Issues](https://github.com/mb43/roamen/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mb43/roamen/discussions)

## Acknowledgements

- **Codec2/FreeDV**: David Rowe and contributors
- **HackRF**: Great Scott Gadgets
- **RTL-SDR**: RTL-SDR.com team
- **Raspberry Pi Foundation**

---

**⚠️ Development Status**: This project is in Phase 1 (Proof of Concept). The protocol and alert system work, but RF integration is not yet complete. Not suitable for production use.

**🏥 Healthcare Use**: If deploying in a healthcare setting, ensure compliance with medical device regulations and data protection laws.
