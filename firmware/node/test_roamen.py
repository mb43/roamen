#!/usr/bin/env python3
"""RoamEN Protocol Test Suite - Prove this shit works!"""

import sys
sys.path.insert(0, '.')

from protocol.packet import RoamENPacket, PacketType, Priority, AlertPacket

def test_basic_packet():
    print("🧪 Testing basic packet creation...")
    
    p1 = RoamENPacket(
        packet_type=PacketType.BEACON,
        source_id=1,
        dest_id=0xFFFF,
        priority=Priority.INFO,
        payload=b"ROAM-01"
    )
    
    data = p1.pack()
    assert len(data) == 32 + 7, f"Wrong size: {len(data)}"
    assert data[:4] == b'ROAM', "Sync word failed"
    
    print(f"  ✅ Packed: {len(data)} bytes")
    return data

def test_unpack(data):
    print("🧪 Testing packet unpacking...")
    
    p2 = RoamENPacket.unpack(data)
    assert p2 is not None, "Unpack failed"
    assert p2.packet_type == PacketType.BEACON
    assert p2.source_id == 1
    assert p2.dest_id == 0xFFFF
    assert p2.payload == b"ROAM-01"
    
    print(f"  ✅ {p2}")

def test_alert():
    print("🧪 Testing alert packet...")
    
    alert = AlertPacket.create(1, 42, 9, "MAYDAY MAYDAY - Fire at TQ123456")
    data = alert.pack()
    
    alert_rx = RoamENPacket.unpack(data)
    assert alert_rx is not None
    
    parsed = AlertPacket.parse(alert_rx)
    assert "MAYDAY" in parsed['message']
    assert alert_rx.priority == Priority.EMERGENCY
    
    print(f"  ✅ Emergency alert: '{parsed['message']}'")
    print(f"  ✅ Priority: {alert_rx.priority.name}")

def test_checksum():
    print("🧪 Testing checksum validation...")
    
    p1 = RoamENPacket(PacketType.TEXT_MESSAGE, 1, 2, Priority.NORMAL, b"Test message")
    data = p1.pack()
    
    # Corrupt a byte in the payload (packet is 32 header + 12 payload = 44 bytes)
    corrupted = bytearray(data)
    corrupted[35] ^= 0xFF  # Corrupt byte 35 (in payload)
    
    p2 = RoamENPacket.unpack(bytes(corrupted))
    assert p2 is None, "Should reject corrupted packet"
    
    print("  ✅ Corruption detected correctly")

def test_addressing():
    print("🧪 Testing broadcast vs unicast...")
    
    broadcast = RoamENPacket(PacketType.BEACON, 1, 0xFFFF)
    assert broadcast.is_for_me(42)
    assert broadcast.is_for_me(99)
    
    unicast = RoamENPacket(PacketType.TEXT_MESSAGE, 1, 42)
    assert unicast.is_for_me(42)
    assert not unicast.is_for_me(99)
    
    print("  ✅ Addressing works")

print("\n" + "="*60)
print("🚀 RoamEN Protocol Test Suite")
print("="*60 + "\n")

try:
    data = test_basic_packet()
    test_unpack(data)
    test_alert()
    test_checksum()
    test_addressing()
    
    print("\n" + "="*60)
    print("🎉 ALL TESTS PASSED! Protocol is WORKING!")
    print("="*60)
    print("\nYour RoamEN protocol is solid. Ready for FreeDV! 🚀\n")
    
except Exception as e:
    print(f"\n❌ TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
