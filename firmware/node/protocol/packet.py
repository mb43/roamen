import struct
import time
from enum import IntEnum
from typing import Optional

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
    EMERGENCY_BROADCAST = 0xFF

class Priority(IntEnum):
    """Message priority levels"""
    INFO = 0
    NORMAL = 1
    URGENT = 2
    EMERGENCY = 9

class RoamENPacket:
    """RoamEN protocol packet with 32-byte header"""
    
    SYNC = b'ROAM'
    VERSION = 0x01
    HEADER_SIZE = 32
    
    def __init__(self, packet_type: PacketType, source_id: int, dest_id: int,
                 priority: Priority = Priority.NORMAL, payload: bytes = b''):
        self.packet_type = packet_type
        self.source_id = source_id
        self.dest_id = dest_id  # 0xFFFF = broadcast
        self.priority = priority
        self.ttl = 5
        self.timestamp = int(time.time())
        self.payload = payload
    
    def pack(self) -> bytes:
        """Pack packet into bytes for transmission"""
        payload_len = len(self.payload)
        
        # Pack header (checksum field = 0 for now)
        header = struct.pack(
            '4s B B H H B B I H H 12x',
            self.SYNC,           # 4 bytes: Sync word
            self.VERSION,        # 1 byte: Protocol version
            self.packet_type,    # 1 byte: Packet type
            self.source_id,      # 2 bytes: Source node ID
            self.dest_id,        # 2 bytes: Destination node ID
            self.priority,       # 1 byte: Priority level
            self.ttl,            # 1 byte: Time to live (hops)
            self.timestamp,      # 4 bytes: Unix timestamp
            payload_len,         # 2 bytes: Payload length
            0                    # 2 bytes: Checksum (calculated next)
        )
        
        # Calculate checksum over header + payload
        checksum = self._crc16(header + self.payload)
        
        # Rebuild header with correct checksum
        header = struct.pack(
            '4s B B H H B B I H H 12x',
            self.SYNC,
            self.VERSION,
            self.packet_type,
            self.source_id,
            self.dest_id,
            self.priority,
            self.ttl,
            self.timestamp,
            payload_len,
            checksum
        )
        
        return header + self.payload
    
    @classmethod
    def unpack(cls, data: bytes) -> Optional['RoamENPacket']:
        """Unpack received bytes into packet"""
        if len(data) < cls.HEADER_SIZE:
            return None
        
        # Unpack header
        header = struct.unpack('4s B B H H B B I H H 12x', data[:cls.HEADER_SIZE])
        
        # Validate sync word
        if header[0] != cls.SYNC:
            return None
        
        # Extract fields
        payload_len = header[8]
        expected_checksum = header[9]
        
        # Validate packet length
        if len(data) < cls.HEADER_SIZE + payload_len:
            return None
        
        # Verify checksum (zero out checksum field first)
        verify_data = data[:18] + b'\x00\x00' + data[20:]
        actual_checksum = cls._crc16(verify_data)
        
        if expected_checksum != actual_checksum:
            print(f"⚠️  Checksum mismatch: expected {expected_checksum}, got {actual_checksum}")
            return None
        
        # Create packet
        packet = cls(
            packet_type=PacketType(header[2]),
            source_id=header[3],
            dest_id=header[4],
            priority=Priority(header[5]),
            payload=data[cls.HEADER_SIZE:cls.HEADER_SIZE + payload_len]
        )
        packet.ttl = header[6]
        packet.timestamp = header[7]
        
        return packet
    
    @staticmethod
    def _crc16(data: bytes) -> int:
        """Calculate CRC16-CCITT checksum"""
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
    
    def is_for_me(self, my_id: int) -> bool:
        """Check if packet is addressed to this node"""
        return self.dest_id == my_id or self.dest_id == 0xFFFF
    
    def __repr__(self):
        return (f"RoamENPacket(type={self.packet_type.name}, "
                f"src={self.source_id}, dst={self.dest_id}, "
                f"pri={self.priority.name}, payload={len(self.payload)}B)")

class AlertPacket:
    """Helper for creating and parsing alert packets"""
    
    @staticmethod
    def create(source_id: int, dest_id: int, alert_type: int, 
               message: str) -> RoamENPacket:
        """Create an alert packet with tone and message"""
        msg_bytes = message.encode('utf-8')[:256]
        
        # Payload: alert_type (1B) + tone_id (1B) + message (256B)
        payload = struct.pack('B B 256s', alert_type, 1, msg_bytes)
        
        # Set priority based on alert type
        if alert_type == 9:
            priority = Priority.EMERGENCY
        elif alert_type == 2:
            priority = Priority.URGENT
        else:
            priority = Priority.NORMAL
        
        return RoamENPacket(
            packet_type=PacketType.ALERT,
            source_id=source_id,
            dest_id=dest_id,
            priority=priority,
            payload=payload
        )
    
    @staticmethod
    def parse(packet: RoamENPacket) -> Optional[dict]:
        """Parse alert packet payload"""
        if packet.packet_type != PacketType.ALERT:
            return None
        
        alert_type, tone_id, msg_bytes = struct.unpack('B B 256s', packet.payload)
        message = msg_bytes.decode('utf-8').rstrip('\x00')
        
        return {
            'alert_type': alert_type,
            'tone_id': tone_id,
            'message': message,
            'source': packet.source_id,
            'priority': packet.priority
        }
