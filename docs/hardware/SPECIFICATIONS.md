# RoamEN Hardware Specifications

## Overview

This document specifies hardware requirements for RoamEN nodes across all deployment phases.

---

## Phase 1: Development Hardware (Current)

### Purpose
Proof of concept and initial development on readily-available hardware.

### Bill of Materials (Per Node)

| Component | Specification | Quantity | Unit Cost | Total |
|-----------|---------------|----------|-----------|-------|
| **Raspberry Pi 4** | 4GB RAM model | 1 | £55 | £55 |
| **MicroSD Card** | 32GB, Class 10, SanDisk Ultra | 1 | £7 | £7 |
| **Power Supply** | Official 5.1V 3A USB-C | 1 | £8 | £8 |
| **HackRF One** | 1MHz-6GHz SDR transceiver | 1 | £220 | £220 |
| **RTL-SDR Blog V3** | Backup RX, spectrum monitoring | 1 | £28 | £28 |
| **USB Sound Card** | Generic USB audio adapter | 1 | £10 | £10 |
| **433MHz Antenna** | SMA male, quarter-wave (17.3cm) | 2 | £10 | £20 |
| **SMA Cables** | Male-male, 30cm | 2 | £5 | £10 |
| **USB Extension** | 2m, USB 2.0 (reduce RFI) | 1 | £5 | £5 |
| **TOTAL** | | | | **£363** |

### Optional Components

| Component | Purpose | Cost |
|-----------|---------|------|
| Heatsinks for Pi | Thermal management | £5 |
| SD card reader | Flashing images | £8 |
| HDMI cable | Pi setup/debugging | £5 |
| USB keyboard/mouse | Pi setup | £15 |
| Portable power bank | Field testing (10,000mAh) | £25 |
| Waterproof case | Outdoor testing | £15 |

### Development Kit (2 Nodes)

**Minimum Setup**: £726 (2× nodes)
**Recommended Setup**: £800 (includes optional items)

---

## Phase 2: Prototype Hardware (Month 4-6)

### Purpose
Custom PCB prototypes for testing and refinement.

### Target Specifications

| Parameter | Specification |
|-----------|---------------|
| **Size** | 90mm × 60mm × 20mm (pager-sized) |
| **Weight** | 120g with battery |
| **Battery Life** | 12-16 hours continuous use |
| **Display** | 0.96" OLED (128×64) or none (phone app) |
| **Connectivity** | Bluetooth 5.0, WiFi (optional) |
| **Interface** | 3 buttons + OLED, or phone app only |
| **Charging** | USB-C, 1 hour fast charge |
| **Durability** | IP54 splash resistant, 1.5m drop test |

### Bill of Materials (Per Prototype)

| Component | Part Number | Quantity | Unit Cost | Total |
|-----------|-------------|----------|-----------|-------|
| **Compute** | | | | |
| Raspberry Pi Zero 2W | - | 1 | £15.00 | £15.00 |
| MicroSD 16GB | - | 1 | £5.00 | £5.00 |
| **Radio** | | | | |
| RFM69HCW 433MHz | RFM69HCW-433S2 | 1 | £10.00 | £10.00 |
| 433MHz PCB antenna | - | 1 | £2.00 | £2.00 |
| SMA connector | - | 1 | £1.00 | £1.00 |
| **Power** | | | | |
| LiPo battery 2000mAh | 3.7V, JST connector | 1 | £8.00 | £8.00 |
| PowerBoost 1000C | Adafruit 2465 | 1 | £12.00 | £12.00 |
| TP4056 charge module | With protection | 1 | £2.00 | £2.00 |
| **Display** (optional) | | | | |
| 0.96" OLED | I2C, SSD1306 | 1 | £5.00 | £5.00 |
| **Interface** | | | | |
| Tactile switches | 6mm, through-hole | 3 | £0.20 | £0.60 |
| Status LEDs | Red, green, blue | 3 | £0.10 | £0.30 |
| LED resistors | 220Ω | 3 | £0.05 | £0.15 |
| **PCB** | | | | |
| Custom PCB | 2-layer, 90×60mm | 1 | £20.00 | £20.00 |
| Headers/connectors | Various | - | £3.00 | £3.00 |
| Passives (caps, res) | Various | - | £2.00 | £2.00 |
| **Enclosure** | | | | |
| 3D printed case | PLA, two-part | 1 | £8.00 | £8.00 |
| **Assembly** | | | | |
| Labor/testing | Manual assembly | 1 | £10.00 | £10.00 |
| **TOTAL** | | | | **£104.05** |

**Without Display**: £99.05
**Prototype Run** (10 units): ~£1,000

---

## Phase 3: Production Hardware (Month 10+)

### Purpose
Volume manufacturing for hospital deployment (5,000 units).

### Cost Targets (Volume Pricing)

| Category | Target Cost | Notes |
|----------|-------------|-------|
| **Compute** | £18 | Pi Zero 2W + SD |
| **Radio** | £10 | RFM69HCW + antenna |
| **Power** | £18 | Battery + charging + boost |
| **Display** | £5 or £0 | Optional OLED or phone-only |
| **PCB** | £8 | 2-layer, volume pricing |
| **Case** | £5 | Injection molding at volume |
| **Assembly** | £8 | Pick-and-place + testing |
| **Accessories** | £5 | Clip, lanyard, USB cable |
| **TOTAL** | **£77** (with display) | Target for 1,000+ units |
| | **£72** (phone-only) | More affordable option |

### Volume Discounts

| Quantity | Cost per Unit | Total Cost |
|----------|---------------|------------|
| 10 | £100 | £1,000 |
| 100 | £85 | £8,500 |
| 1,000 | £77 | £77,000 |
| 5,000 | £72 | £360,000 |

**5,000 unit production**: £360,000 (£72/unit)
**With spares/accessories**: £385,000 total

---

## Fixed Infrastructure Nodes

### Purpose
Always-on mesh backbone for hospital coverage.

### Specification

| Component | Specification | Quantity | Unit Cost | Total |
|-----------|---------------|----------|-----------|-------|
| **Compute** | Raspberry Pi 4 (4GB) | 1 | £55 | £55 |
| **Radio** | HackRF One | 1 | £220 | £220 |
| **Power** | 12V DC power supply | 1 | £15 | £15 |
| **Antenna** | High-gain 433MHz (6dBi) | 1 | £25 | £25 |
| **Cable** | LMR-400 coax, 10m | 1 | £30 | £30 |
| **Mounting** | Weatherproof enclosure + bracket | 1 | £40 | £40 |
| **Network** | Ethernet cable/PoE (optional) | 1 | £20 | £20 |
| **TOTAL** | | | | **£405** |

**50-node deployment**: £20,250
**With installation/cabling**: £25,000

### Placement Recommendations

**Optimal Locations**:
- Building rooftops (highest point)
- Top floors of multi-story buildings
- Central corridors on each floor
- Departmental high points (A&E, ICU, etc.)

**Spacing**:
- Urban: 50-100m between nodes
- Redundancy: 2-3× coverage overlap
- Vertical: One node per 2-3 floors

**Antenna Considerations**:
- Omnidirectional for general coverage
- Directional for long corridors
- Height: 2m+ above floor level
- Clearance: Away from metal obstacles

---

## Accessories and Spares

### Charging Stations

| Item | Specification | Quantity | Cost |
|------|---------------|----------|------|
| 10-port USB charger | 2.4A per port | 5 | £50 |
| USB-C cables | 30cm, pack of 10 | 50 | £200 |
| Charging rack | 3D printed, 10 slots | 50 | £500 |
| **TOTAL** | | | **£750** |

### Spare Parts (2% attrition rate)

| Item | Quantity | Cost |
|------|----------|------|
| Complete spare nodes | 100 | £7,200 |
| Replacement batteries | 200 | £1,600 |
| Replacement cases | 100 | £500 |
| Charging cables | 500 | £1,000 |
| **TOTAL** | | **£10,300** |

---

## Testing Equipment

### Required for Development

| Item | Purpose | Cost |
|------|---------|------|
| Spectrum analyzer | Verify RF output | £500 |
| RF power meter | Measure TX power | £150 |
| Multimeter | General testing | £50 |
| Oscilloscope | Signal debugging | £400 |
| Soldering station | Assembly/repair | £100 |
| 3D printer | Case prototyping | £300 |
| **TOTAL** | | **£1,500** |

### Quality Control (Production)

| Item | Purpose | Quantity | Cost |
|------|---------|----------|------|
| RF test fixture | Automated RF testing | 1 | £2,000 |
| Battery tester | Capacity verification | 1 | £500 |
| Functional test jig | Automated testing | 2 | £1,000 |
| **TOTAL** | | | **£3,500** |

---

## Environmental Specifications

### Operating Conditions

| Parameter | Specification |
|-----------|---------------|
| **Temperature** | 0°C to +40°C (operational) |
| | -20°C to +60°C (storage) |
| **Humidity** | 10% to 90% RH (non-condensing) |
| **Altitude** | 0 to 2,000m |
| **Ingress Protection** | IP54 (splash resistant) |
| **Drop Test** | 1.5m onto concrete |
| **Vibration** | IEC 60068-2-6 (transport) |

### Battery Specifications

| Parameter | Specification |
|-----------|---------------|
| **Chemistry** | LiPo (Lithium Polymer) |
| **Capacity** | 2000mAh minimum |
| **Voltage** | 3.7V nominal (3.0-4.2V) |
| **Charge Rate** | 1C (2A) maximum |
| **Protection** | Over-charge, over-discharge, short-circuit |
| **Cycle Life** | 500 cycles to 80% capacity |
| **Replacement** | Every 18-24 months |

### Power Consumption

| Mode | Current Draw | Duration | Notes |
|------|--------------|----------|-------|
| **Idle (RX)** | 150mA @ 3.7V | Continuous | Listening only |
| **Voice RX** | 200mA @ 3.7V | During receive | Speaker + decode |
| **Voice TX** | 400mA @ 3.7V | During transmit | 10mW RF + encode |
| **Beacon TX** | 350mA @ 3.7V | 100ms every 30s | Periodic |
| **Sleep** | 50mA @ 3.7V | When inactive | Display off |

**Battery Life Calculation** (2000mAh battery):
- Continuous RX: 13.3 hours
- Typical use (70% RX, 20% TX, 10% idle): 11.5 hours
- Target: 12+ hours per charge ✅

---

## Radio Specifications

### Frequency

| Parameter | Specification |
|-----------|---------------|
| **Band** | 433MHz ISM |
| **Frequency** | 433.500 MHz (center) |
| **Channels** | 4 (433.05, 433.50, 433.95, 434.40 MHz) |
| **Bandwidth** | 25 kHz per channel |
| **Regulation** | UK IR 2030, EU ETSI EN 300 220 |

### RF Performance

| Parameter | Specification |
|-----------|---------------|
| **TX Power** | 10mW ERP (10 dBm) maximum |
| **RX Sensitivity** | -110 dBm |
| **Modulation** | FSK (Frequency Shift Keying) |
| **Data Rate** | 4800 bps |
| **Range** | 1-3km urban, 5km rural (line of sight) |

### Antenna

| Parameter | Specification |
|-----------|---------------|
| **Type** | Quarter-wave whip or PCB antenna |
| **Length** | 17.3cm (quarter-wave @ 433MHz) |
| **Connector** | SMA male (external) or PCB (internal) |
| **Gain** | 0 dBi (whip), -2 dBi (PCB) |
| **Impedance** | 50Ω |
| **VSWR** | <1.5:1 @ 433MHz |

---

## Compliance and Certification

### Required Certifications

| Standard | Requirement | Status |
|----------|-------------|--------|
| **CE Marking** | EU compliance | Required for production |
| **UKCA** | UK compliance (post-Brexit) | Required for UK |
| **FCC Part 15** | USA (if exported) | Not required for UK-only |
| **Medical Device** | Depends on classification | Under review |

### Testing Required

| Test | Standard | Purpose |
|------|----------|---------|
| **EMC** | EN 301 489 | Electromagnetic compatibility |
| **Radio** | EN 300 220 | 433MHz operation |
| **Safety** | EN 60950 | Electrical safety |
| **Environmental** | IEC 60068 | Reliability |

**Estimated Certification Cost**: £10,000-£15,000

---

## Supply Chain

### Key Components

| Component | Supplier | Lead Time | MOQ |
|-----------|----------|-----------|-----|
| Raspberry Pi Zero 2W | Approved distributors | 4-8 weeks | 1 |
| RFM69HCW | Digi-Key, Mouser, RS | 2-4 weeks | 1 |
| LiPo batteries | UK battery suppliers | 4-6 weeks | 100 |
| PCBs | JLCPCB, PCBWay | 2 weeks | 5 |
| 3D printing/injection | UK manufacturers | 2-8 weeks | 10/1000 |

### Risk Mitigation

**Component Shortages**:
- Maintain 10% buffer stock
- Multiple approved suppliers
- Alternative components identified

**Lead Times**:
- Order long-lead items early (Pi, batteries)
- Build buffer into project plan
- Prototype with available stock

---

## Manufacturing Plan

### Phase 1: Prototype (10 units)

**Approach**: Manual assembly
**Location**: In-house or contract assembler
**Timeline**: 2 weeks
**Cost**: £100/unit

### Phase 2: Pilot (100 units)

**Approach**: Semi-automated assembly
**Location**: UK contract manufacturer
**Timeline**: 4 weeks
**Cost**: £85/unit

### Phase 3: Production (5,000 units)

**Approach**: Fully automated (pick-and-place)
**Location**: UK or EU manufacturer
**Timeline**: 12 weeks
**Cost**: £72/unit

**Quality Control**:
- 100% functional testing
- Random RF testing (10%)
- Battery capacity testing (10%)
- Drop testing (sample)
- IP rating verification (sample)

---

## Maintenance and Support

### Consumables

| Item | Replacement Interval | Cost/Unit |
|------|----------------------|-----------|
| Battery | 18-24 months | £8 |
| USB cable | As needed | £2 |
| Antenna | Rarely (damage only) | £10 |

### Repair Strategy

**Level 1** (User):
- Battery replacement
- Charging cable replacement
- Basic troubleshooting

**Level 2** (IT/Estates):
- Firmware updates
- Configuration changes
- Device replacement from spares

**Level 3** (Manufacturer):
- PCB repair
- Component replacement
- Advanced diagnostics

**Target**: 95% repairs at Level 1-2

---

## Future Enhancements

### Version 2 Hardware (18-24 months)

**Improvements**:
- Custom system-on-module (SoM) instead of Pi
- Integrated display + radio module
- Smaller form factor (phone-sized)
- Longer battery life (20+ hours)
- Better RF performance
- GPS module
- Improved case (injection molded)

**Target Cost**: £50/unit @ 10,000 quantity

### Advanced Features

- LoRa mode (long range, lower bandwidth)
- Dual-band (433MHz + 868MHz)
- Satellite uplink (emergencies)
- Solar charging (fixed nodes)
- Temperature sensor (building monitoring)

---

**Document Version**: 1.0
**Last Updated**: 2025-11-19
**Status**: Phase 1 - Development
