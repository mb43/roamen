# RoamEN Protocol Specification v0.1

## 1. Introduction

### 1.1 Purpose
RoamEN (Roaming Emergency Network) protocol provides reliable, priority-based communication for emergency scenarios where traditional infrastructure fails.

### 1.2 Design Goals
- **Simplicity**: Easy to implement and debug
- **Reliability**: Error detection and correction
- **Efficiency**: Minimal overhead for low-bandwidth links
- **Priority**: Critical messages delivered first
- **Flexibility**: Support multiple message types

### 1.3 Scope
This specification covers:
- Packet format and encoding
- Message types and semantics
- Error detection mechanisms
- Addressing and routing basics

Future versions will cover:
- Encryption and authentication
- Advanced routing protocols
- Quality of Service (QoS)

## 2. Packet Structure

### 2.1 General Format

All RoamEN packets consist of:
```
┌─────────────┬──────────────────────┐
│   Header    │       Payload        │
│  (32 bytes) │    (0-N bytes)       │
└─────────────┴──────────────────────┘
```

### 2.2 Header Format

The header is fixed at 32 bytes:

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       SYNC ('ROAM')                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   VERSION     |     TYPE      |          SOURCE_ID            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           DEST_ID             |   PRIORITY    |      TTL      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          TIMESTAMP                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|        PAYLOAD_LENGTH         |           CHECKSUM            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                         RESERVED (12 bytes)                   |
|                                                               |
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### 2.3 Header Fields

| Field | Offset | Size | Type | Description |
|-------|--------|------|------|-------------|
| SYNC | 0 | 4 | bytes | Magic bytes: 'ROAM' (0x52 0x4F 0x41 0x4D) |
| VERSION | 4 | 1 | uint8 | Protocol version (currently 0x01) |
| TYPE | 5 | 1 | uint8 | Packet type (see section 3) |
| SOURCE_ID | 6 | 2 | uint16 | Source node identifier (big-endian) |
| DEST_ID | 8 | 2 | uint16 | Destination node identifier (big-endian) |
| PRIORITY | 10 | 1 | uint8 | Message priority (0-9) |
| TTL | 11 | 1 | uint8 | Time to live (hop count) |
| TIMESTAMP | 12 | 4 | uint32 | Unix timestamp (big-endian) |
| PAYLOAD_LENGTH | 16 | 2 | uint16 | Length of payload in bytes (big-endian) |
| CHECKSUM | 18 | 2 | uint16 | CRC16-CCITT (big-endian) |
| RESERVED | 20 | 12 | bytes | Reserved for future use (must be zero) |

### 2.4 Field Definitions

#### 2.4.1 SYNC Word
- Fixed value: 'ROAM' (0x52 0x4F 0x41 0x4D)
- Used for packet synchronization
- Receivers scan for this pattern

#### 2.4.2 VERSION
- Current version: 0x01
- Increments for incompatible changes
- Receivers must reject unknown versions

#### 2.4.3 SOURCE_ID / DEST_ID
- Range: 0x0001 to 0xFFFE (1 to 65534)
- 0x0000: Reserved (invalid)
- 0xFFFF: Broadcast address
- Big-endian byte order

#### 2.4.4 PRIORITY
| Value | Name | Usage |
|-------|------|-------|
| 0 | INFO | Beacons, routine status |
| 1 | NORMAL | Regular messages |
| 2 | URGENT | Important notifications |
| 3-8 | Reserved | Future use |
| 9 | EMERGENCY | Life-threatening situations |

Higher priority messages should be transmitted first.

#### 2.4.5 TTL (Time To Live)
- Hop count for mesh routing
- Decremented by each relay
- Packet dropped when TTL reaches 0
- Recommended initial value: 5

#### 2.4.6 TIMESTAMP
- Unix timestamp (seconds since 1970-01-01 00:00:00 UTC)
- 32-bit unsigned integer
- Used for:
  - Message ordering
  - Duplicate detection
  - Network time synchronization

#### 2.4.7 PAYLOAD_LENGTH
- Length of payload in bytes
- Maximum value: Implementation defined (recommended: 256)
- Zero is valid (header-only packet)

#### 2.4.8 CHECKSUM
- CRC16-CCITT algorithm
- Polynomial: 0x1021
- Initial value: 0xFFFF
- Computed over: Entire packet with checksum field set to 0
- Receivers must validate and reject if mismatch

## 3. Packet Types

### 3.1 Type Definitions

| Type | Value | Name | Description |
|------|-------|------|-------------|
| 0x00 | - | RESERVED | Invalid/reserved |
| 0x01 | 1 | BEACON | Network presence announcement |
| 0x02 | 2 | TEXT_MESSAGE | Text/chat message |
| 0x03 | 3 | VOICE_START | Voice transmission start |
| 0x04 | 4 | VOICE_DATA | Voice data chunk |
| 0x05 | 5 | VOICE_END | Voice transmission end |
| 0x06 | 6 | ALERT | Selective call/alert |
| 0x07 | 7 | ACK | Acknowledgement |
| 0x08-0x0F | - | RESERVED | Reserved for protocol use |
| 0x10 | 16 | FILE_CHUNK | File transfer chunk |
| 0x11-0xFE | - | RESERVED | Reserved for future use |
| 0xFF | 255 | EMERGENCY_BROADCAST | Emergency override |

### 3.2 BEACON (0x01)

**Purpose**: Announce node presence and capabilities

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Callsign (16 bytes)                       |
|                         ...                                   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Capabilities |                  Reserved                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- Callsign: UTF-8 string, null-padded
- Capabilities: Bitfield (future use)

**Usage**:
- Sent periodically (default: every 30 seconds)
- Broadcast (DEST_ID = 0xFFFF)
- Priority: INFO

### 3.3 TEXT_MESSAGE (0x02)

**Purpose**: Send text messages

**Payload Format**:
- UTF-8 encoded text
- Maximum length: Implementation defined (recommended: 256 bytes)
- No null termination required

**Usage**:
- Can be unicast or broadcast
- Priority: Typically NORMAL, can be higher

### 3.4 VOICE_START (0x03)

**Purpose**: Initiate voice transmission

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   Codec Type  |     Flags     |          Session ID           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- Codec Type: Voice codec identifier (0x01 = Codec2)
- Flags: Reserved
- Session ID: Unique identifier for this voice session

**Usage**:
- Sent before VOICE_DATA packets
- Receivers prepare audio output

### 3.5 VOICE_DATA (0x04)

**Purpose**: Carry voice data

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Session ID           |       Sequence Number         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                      Voice Data (variable)                    |
|                             ...                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- Session ID: Must match VOICE_START
- Sequence Number: Increments for each frame
- Voice Data: Encoded audio (Codec2 format)

**Usage**:
- Sent repeatedly during voice transmission
- Sequence number allows gap detection

### 3.6 VOICE_END (0x05)

**Purpose**: End voice transmission

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Session ID           |         Final Sequence        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- Session ID: Must match VOICE_START
- Final Sequence: Last sequence number sent

**Usage**:
- Signals end of voice transmission
- Receivers close audio channel

### 3.7 ALERT (0x06)

**Purpose**: Selective calling and alerts

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   Alert Type  |    Tone ID    |                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +
|                     Message (256 bytes)                       |
|                             ...                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- Alert Type: 0-9 (maps to priority)
- Tone ID: Alert tone to play
  - 1 = Standard (two-tone beep)
  - 2 = Urgent (warbling)
  - 3 = Emergency (aggressive siren)
- Message: UTF-8 text, null-padded

**Priority Mapping**:
- Alert Type 9 → EMERGENCY priority
- Alert Type 2 → URGENT priority
- Others → NORMAL priority

**Usage**:
- Can be unicast (specific person) or broadcast (department)
- Triggers audio alert on receiver
- Message displayed to user

### 3.8 ACK (0x07)

**Purpose**: Acknowledge packet receipt

**Payload Format**:
```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    ACK'd Timestamp                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           ACK'd Source        |       Status Code             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

**Fields**:
- ACK'd Timestamp: Timestamp of packet being acknowledged
- ACK'd Source: Source ID of packet being acknowledged
- Status Code: 0 = Success, >0 = Error codes

**Usage**:
- Optional confirmation of delivery
- Can trigger retransmission if not received

### 3.9 EMERGENCY_BROADCAST (0xFF)

**Purpose**: Override all other traffic

**Payload Format**:
- UTF-8 encoded emergency message
- Maximum length: 256 bytes

**Usage**:
- Always EMERGENCY priority
- Always broadcast (DEST_ID = 0xFFFF)
- Receivers must display immediately
- Triggers emergency alert tone
- Examples: "EVACUATE BUILDING", "CODE RED"

## 4. Error Detection

### 4.1 CRC16-CCITT Algorithm

**Polynomial**: 0x1021 (x^16 + x^12 + x^5 + 1)
**Initial Value**: 0xFFFF
**Final XOR**: None

**Python Implementation**:
```python
def crc16_ccitt(data: bytes) -> int:
    crc = 0xFFFF
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc
```

### 4.2 Checksum Validation

**Sender**:
1. Set checksum field to 0
2. Calculate CRC over entire packet (header + payload)
3. Write CRC to checksum field

**Receiver**:
1. Extract received checksum
2. Set checksum field to 0
3. Calculate CRC over entire packet
4. Compare with received checksum
5. Reject if mismatch

### 4.3 Error Handling

**On Checksum Failure**:
- Silently drop packet
- Do not acknowledge
- Optionally log for debugging

**On Unknown Packet Type**:
- Silently drop packet
- Log warning

**On Invalid Field Values**:
- Drop packet if critical (e.g., invalid SOURCE_ID)
- Use defaults if non-critical

## 5. Addressing and Routing

### 5.1 Node IDs

**Valid Range**: 0x0001 to 0xFFFE (1 to 65534)

**Special Addresses**:
- 0x0000: Invalid/unassigned
- 0xFFFF: Broadcast

**Assignment**:
- Statically configured
- Must be unique within network
- Recommended: Sequential assignment by department/role

### 5.2 Broadcast

**Destination**: 0xFFFF

**Behavior**:
- All nodes receive and process
- Not relayed (to prevent loops)
- Examples: Beacons, emergency broadcasts

### 5.3 Unicast

**Destination**: Specific node ID

**Behavior**:
- Only addressed node processes
- Other nodes may relay if implementing mesh
- TTL decremented on each hop

### 5.4 Basic Relay (Future)

When implementing mesh routing:
1. Receive packet
2. Check if for this node
3. If yes: Process locally
4. If no and TTL > 0:
   - Decrement TTL
   - Recalculate checksum
   - Retransmit

## 6. Network Behavior

### 6.1 Beacons

**Frequency**: Every 30 seconds (configurable)
**Purpose**: Network discovery, presence indication
**Priority**: INFO
**Format**: BEACON packet type

### 6.2 Buddy System

**Timeout**: 300 seconds (5 minutes)
**Behavior**:
- Mark node as offline if no beacon received
- Display warning to user
- Remove from routing tables

### 6.3 Time Synchronization

**Mechanism**: Timestamp in every packet
**Accuracy**: ±30 seconds acceptable
**Usage**:
- Message ordering
- Duplicate detection
- Event correlation

## 7. Implementation Notes

### 7.1 Byte Order

**All multi-byte fields**: Big-endian (network byte order)

**Example** (SOURCE_ID = 42):
- Byte 6: 0x00
- Byte 7: 0x2A

### 7.2 Payload Constraints

**Recommended Maximum**: 256 bytes
**Reason**: Balance between:
- Transmission time
- Buffer requirements
- Error probability

### 7.3 Buffer Sizes

**Minimum RX Buffer**: Header size + max payload
**Recommended**: 512 bytes (allows headroom)

### 7.4 Timing

**Beacon Interval**: 30 seconds
**ACK Timeout**: 5 seconds
**Retry Delay**: 1 second
**Max Retries**: 3

## 8. Examples

### 8.1 Simple Beacon

```
Header:
  SYNC: 'ROAM' (0x52 0x4F 0x41 0x4D)
  VERSION: 0x01
  TYPE: 0x01 (BEACON)
  SOURCE_ID: 0x0001 (1)
  DEST_ID: 0xFFFF (broadcast)
  PRIORITY: 0 (INFO)
  TTL: 5
  TIMESTAMP: 0x6740B2C0 (current time)
  PAYLOAD_LENGTH: 0x0010 (16 bytes)
  CHECKSUM: 0xABCD (calculated)
  RESERVED: all zeros

Payload:
  "ROAM-01\0\0\0\0\0\0\0\0\0" (callsign, null-padded)
```

### 8.2 Emergency Alert

```
Header:
  SYNC: 'ROAM'
  VERSION: 0x01
  TYPE: 0x06 (ALERT)
  SOURCE_ID: 0x0001
  DEST_ID: 0xFFFF (broadcast)
  PRIORITY: 9 (EMERGENCY)
  TTL: 5
  TIMESTAMP: (current)
  PAYLOAD_LENGTH: 0x0102 (258 bytes)
  CHECKSUM: (calculated)

Payload:
  Alert Type: 9 (emergency)
  Tone ID: 3 (aggressive siren)
  Message: "EVACUATE BUILDING - FIRE IN EAST WING"
```

### 8.3 Text Message

```
Header:
  SYNC: 'ROAM'
  VERSION: 0x01
  TYPE: 0x02 (TEXT_MESSAGE)
  SOURCE_ID: 0x0042
  DEST_ID: 0x0017 (specific person)
  PRIORITY: 1 (NORMAL)
  TTL: 5
  TIMESTAMP: (current)
  PAYLOAD_LENGTH: 0x001A (26 bytes)
  CHECKSUM: (calculated)

Payload:
  "Patient in bed 3 ready"
```

## 9. Security Considerations

### 9.1 Current Status (v0.1)
- ❌ No encryption - all traffic in clear text
- ❌ No authentication - anyone can send packets
- ⚠️ Suitable for proof of concept only
- ⚠️ NOT suitable for sensitive data

### 9.2 Future Versions
- AES-256 encryption planned
- Message authentication codes (MAC)
- Key distribution protocol
- Perfect forward secrecy

### 9.3 Recommendations
- Use only in controlled environments
- No patient data in current version
- Assume all traffic is monitored
- Plan for encryption before production

## 10. Compliance

### 10.1 Regulatory
- **UK**: IR 2030 (433MHz ISM band)
- **Max Power**: 10mW ERP
- **Duty Cycle**: <10% (not enforced at protocol level)

### 10.2 Medical Device
- Future certification required
- Patient safety considerations
- Data protection compliance

## 11. Version History

### v0.1 (Current)
- Initial protocol definition
- Basic packet types
- CRC16 error detection
- No encryption

### v0.2 (Planned)
- Add encryption
- Enhanced routing
- QoS mechanisms

---

**Document Version**: 1.0
**Protocol Version**: 0.1
**Status**: Phase 1 - MVP
**Last Updated**: 2025-11-19
