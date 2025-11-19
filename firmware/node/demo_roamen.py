#!/usr/bin/env python3
"""
RoamEN Interactive Demo

This script demonstrates how RoamEN nodes communicate in a simulated environment.
Run this to see the protocol in action without needing actual radio hardware.
"""

import sys
import time
import random
from protocol.packet import RoamENPacket, PacketType, Priority, AlertPacket

# ANSI color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_header(text):
    """Print a colorful header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")

def print_node(node_id, text, color=Colors.GREEN):
    """Print a message from a node"""
    node_name = f"[Node {node_id:02d}]"
    print(f"{color}{Colors.BOLD}{node_name:12}{Colors.END} {text}")

def print_packet(packet, direction="→"):
    """Print packet details"""
    type_colors = {
        PacketType.BEACON: Colors.CYAN,
        PacketType.TEXT_MESSAGE: Colors.GREEN,
        PacketType.VOICE_START: Colors.BLUE,
        PacketType.VOICE_DATA: Colors.BLUE,
        PacketType.VOICE_END: Colors.BLUE,
        PacketType.ALERT: Colors.YELLOW if packet.priority != Priority.EMERGENCY else Colors.RED,
        PacketType.ACK: Colors.GREEN,
        PacketType.EMERGENCY_BROADCAST: Colors.RED,
    }

    color = type_colors.get(packet.packet_type, Colors.END)

    dest = "BROADCAST" if packet.dest_id == 0xFFFF else f"Node {packet.dest_id:02d}"

    print(f"  {color}{direction} {packet.packet_type.name:20} "
          f"src:{packet.source_id:02d} → dst:{dest:12} "
          f"pri:{packet.priority.name:9} "
          f"size:{len(packet.payload):3}B{Colors.END}")

def simulate_network_delay():
    """Simulate radio transmission time"""
    time.sleep(random.uniform(0.05, 0.15))

def demo_basic_beacon():
    """Demo 1: Basic beacon transmission"""
    print_header("DEMO 1: Network Beacon")

    print("Nodes announce their presence periodically with beacon packets.\n")

    # Node 1 sends beacon
    print_node(1, "Sending beacon...")
    beacon = RoamENPacket(
        packet_type=PacketType.BEACON,
        source_id=1,
        dest_id=0xFFFF,  # Broadcast
        priority=Priority.INFO,
        payload=b"ROAM-01"
    )

    data = beacon.pack()
    print_packet(beacon, "📡")

    simulate_network_delay()

    # Other nodes receive it
    print_node(2, f"Received beacon from Node 01 (signal: strong)")
    print_node(5, f"Received beacon from Node 01 (signal: medium)")
    print_node(8, f"Received beacon from Node 01 (signal: weak)")

    print(f"\n{Colors.CYAN}Result: All nodes know Node 01 is online{Colors.END}")

def demo_text_message():
    """Demo 2: Text messaging"""
    print_header("DEMO 2: Text Messaging")

    print("Staff send text messages to coordinate patient care.\n")

    # Node 5 (Pharmacy) sends to Node 12 (Ward)
    print_node(5, "Pharmacy → Ward: Sending message...")
    message = RoamENPacket(
        packet_type=PacketType.TEXT_MESSAGE,
        source_id=5,
        dest_id=12,
        priority=Priority.NORMAL,
        payload=b"Controlled drugs for bed 3 ready for collection"
    )

    data = message.pack()
    print_packet(message, "💬")

    simulate_network_delay()

    # Node 12 receives
    received = RoamENPacket.unpack(data)
    msg_text = received.payload.decode('utf-8')
    print_node(12, f"Received: '{msg_text}'")

    # Node 12 sends ACK
    print_node(12, "Sending acknowledgement...")
    ack = RoamENPacket(
        packet_type=PacketType.ACK,
        source_id=12,
        dest_id=5,
        priority=Priority.NORMAL,
        payload=b"Message received"
    )
    print_packet(ack, "✅")

    simulate_network_delay()

    print_node(5, "ACK received - message delivered!")

    print(f"\n{Colors.GREEN}Result: Reliable message delivery confirmed{Colors.END}")

def demo_voice_transmission():
    """Demo 3: Voice call"""
    print_header("DEMO 3: Voice Transmission")

    print("A&E coordinator makes voice announcement to department.\n")

    # Voice START
    print_node(1, "A&E Coordinator: Press PTT button")
    voice_start = RoamENPacket(
        packet_type=PacketType.VOICE_START,
        source_id=1,
        dest_id=0xFFFF,  # Broadcast to all
        priority=Priority.URGENT,
        payload=b"\x01\x00\x2A\x00"  # Codec=Codec2, Session=42
    )
    print_packet(voice_start, "🎤")

    simulate_network_delay()

    print_node(2, "📻 Voice RX started - playing audio...")
    print_node(3, "📻 Voice RX started - playing audio...")
    print_node(4, "📻 Voice RX started - playing audio...")

    # Voice DATA (simulated 3 packets)
    print(f"\n{Colors.BLUE}Transmitting voice data...{Colors.END}")
    for i in range(3):
        voice_data = RoamENPacket(
            packet_type=PacketType.VOICE_DATA,
            source_id=1,
            dest_id=0xFFFF,
            priority=Priority.URGENT,
            payload=f"Voice frame {i}".encode()
        )
        print_packet(voice_data, "🔊")
        simulate_network_delay()

    # Voice END
    voice_end = RoamENPacket(
        packet_type=PacketType.VOICE_END,
        source_id=1,
        dest_id=0xFFFF,
        priority=Priority.URGENT,
        payload=b"\x2A\x00\x03\x00"  # Session=42, Final_seq=3
    )
    print_node(1, "Released PTT button")
    print_packet(voice_end, "🛑")

    simulate_network_delay()

    print_node(2, "📻 Voice RX ended")
    print_node(3, "📻 Voice RX ended")
    print_node(4, "📻 Voice RX ended")

    print(f"\n{Colors.BLUE}Message heard: \"Patient in bed 12 needs immediate assessment\"{Colors.END}")
    print(f"{Colors.GREEN}Result: Voice message broadcast to all A&E staff{Colors.END}")

def demo_alert_standard():
    """Demo 4: Standard alert"""
    print_header("DEMO 4: Standard Priority Alert")

    print("Non-urgent notification sent to specific staff member.\n")

    print_node(7, "Sending standard alert to Node 15...")
    alert = AlertPacket.create(
        source_id=7,
        dest_id=15,
        alert_type=1,  # Standard
        message="Your break ends in 5 minutes"
    )

    data = alert.pack()
    print_packet(alert, "🔔")

    simulate_network_delay()

    received = RoamENPacket.unpack(data)
    parsed = AlertPacket.parse(received)

    print_node(15, f"🔔 Alert tone: beep-beep (standard.wav)")
    print_node(15, f"Display: '{parsed['message']}'")
    print_node(15, "User pressed ACK button")

    print(f"\n{Colors.CYAN}Result: Staff notified, alert acknowledged{Colors.END}")

def demo_alert_urgent():
    """Demo 5: Urgent alert"""
    print_header("DEMO 5: Urgent Priority Alert")

    print("Time-sensitive alert broadcast to department.\n")

    print_node(2, "ICU Coordinator: Sending urgent alert...")
    alert = AlertPacket.create(
        source_id=2,
        dest_id=0xFFFF,  # Broadcast
        alert_type=2,  # Urgent
        message="Code Blue - Bed 7 - All available staff respond"
    )

    data = alert.pack()
    print_packet(alert, "⚠️")

    simulate_network_delay()

    # Multiple nodes receive
    received = RoamENPacket.unpack(data)
    parsed = AlertPacket.parse(received)

    print_node(3, f"⚠️  Alert tone: wee-woo-wee-woo (urgent.wav)")
    print_node(4, f"⚠️  Alert tone: wee-woo-wee-woo (urgent.wav)")
    print_node(5, f"⚠️  Alert tone: wee-woo-wee-woo (urgent.wav)")

    print(f"\n{Colors.YELLOW}Display on all nodes:{Colors.END}")
    print(f"  {Colors.YELLOW}'{parsed['message']}'{Colors.END}")

    time.sleep(0.5)

    print_node(3, "Responding - en route to Bed 7")
    print_node(5, "Responding - bringing crash cart")

    print(f"\n{Colors.YELLOW}Result: Emergency team mobilized within seconds{Colors.END}")

def demo_alert_emergency():
    """Demo 6: Emergency broadcast"""
    print_header("DEMO 6: EMERGENCY BROADCAST")

    print("Critical facility-wide emergency alert.\n")

    time.sleep(0.5)

    print_node(1, f"{Colors.RED}EMERGENCY CONTROL: Broadcasting critical alert...{Colors.END}")
    alert = AlertPacket.create(
        source_id=1,
        dest_id=0xFFFF,  # Broadcast to ALL
        alert_type=9,  # Emergency
        message="FIRE ALARM - EAST WING - EVACUATE IMMEDIATELY"
    )

    data = alert.pack()
    print_packet(alert, "🚨")

    simulate_network_delay()

    # ALL nodes receive and respond
    received = RoamENPacket.unpack(data)
    parsed = AlertPacket.parse(received)

    print(f"\n{Colors.RED}{Colors.BOLD}*** ALL DEVICES ALARM SIMULTANEOUSLY ***{Colors.END}")
    print(f"{Colors.RED}🚨 WEE-WOO-WEE-WOO-WEE-WOO (LOUD){Colors.END}")

    time.sleep(0.3)

    print(f"\n{Colors.RED}Full screen takeover on all devices:{Colors.END}")
    print(f"{Colors.RED}╔══════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.RED}║  🚨 EMERGENCY 🚨                     ║{Colors.END}")
    print(f"{Colors.RED}║                                      ║{Colors.END}")
    print(f"{Colors.RED}║  {parsed['message']:36} ║{Colors.END}")
    print(f"{Colors.RED}║                                      ║{Colors.END}")
    print(f"{Colors.RED}║  [ACKNOWLEDGE]                       ║{Colors.END}")
    print(f"{Colors.RED}╚══════════════════════════════════════╝{Colors.END}")

    time.sleep(0.5)

    print("\nStaff responses:")
    print_node(2, f"{Colors.RED}Acknowledged - Evacuating ICU patients{Colors.END}")
    print_node(3, f"{Colors.RED}Acknowledged - Closing fire doors{Colors.END}")
    print_node(5, f"{Colors.RED}Acknowledged - Assisting in Ward A{Colors.END}")
    print_node(8, f"{Colors.RED}Acknowledged - Clear of building{Colors.END}")

    print(f"\n{Colors.RED}{Colors.BOLD}Result: All 50 staff alerted and evacuating - potential lives saved{Colors.END}")

def demo_network_failure():
    """Demo 7: Communication during IT failure"""
    print_header("DEMO 7: IT Infrastructure Failure")

    print("Simulating major IT outage - RoamEN remains operational.\n")

    print(f"{Colors.RED}❌ Hospital WiFi: DOWN{Colors.END}")
    print(f"{Colors.RED}❌ PABX Phones: DOWN{Colors.END}")
    print(f"{Colors.RED}❌ Mobile Network: CONGESTED{Colors.END}")
    print(f"{Colors.RED}❌ Paging System: DOWN{Colors.END}")

    time.sleep(0.5)

    print(f"\n{Colors.GREEN}✅ RoamEN Network: OPERATIONAL (Independent){Colors.END}")

    # Beacons continue
    print("\nNetwork beacons continue every 30 seconds:")
    for i in range(1, 6):
        beacon = RoamENPacket(
            packet_type=PacketType.BEACON,
            source_id=i,
            dest_id=0xFFFF,
            payload=f"ROAM-{i:02d}".encode()
        )
        print_packet(beacon, "📡")
        time.sleep(0.2)

    print(f"\n{Colors.GREEN}All RoamEN nodes confirm: Network healthy{Colors.END}")

    # Staff can still communicate
    print("\nStaff communications continue:")

    msg1 = RoamENPacket(
        packet_type=PacketType.TEXT_MESSAGE,
        source_id=5,
        dest_id=12,
        payload=b"IT systems down - use RoamEN for all comms"
    )
    print_packet(msg1, "💬")

    msg2 = RoamENPacket(
        packet_type=PacketType.TEXT_MESSAGE,
        source_id=12,
        dest_id=5,
        payload=b"Confirmed - switching to RoamEN only"
    )
    print_packet(msg2, "💬")

    print(f"\n{Colors.GREEN}{Colors.BOLD}Result: Hospital operations continue despite IT failure{Colors.END}")
    print(f"{Colors.GREEN}Patient care uninterrupted - RoamEN provides communication continuity{Colors.END}")

def demo_mesh_routing():
    """Demo 8: Mesh network routing"""
    print_header("DEMO 8: Mesh Network Routing")

    print("Message automatically routed through intermediate nodes.\n")

    print("Network topology:")
    print("""
        Node 1 ─────── Node 5 ─────── Node 9
          │                             │
          │                             │
        Node 3                        Node 12
          │
          │
        Node 7 (out of range from Node 12)
    """)

    print("\nNode 7 wants to send to Node 12 (out of direct range)...\n")

    # Node 7 sends to Node 12
    print_node(7, "Sending message to Node 12 (TTL=5)...")
    message = RoamENPacket(
        packet_type=PacketType.TEXT_MESSAGE,
        source_id=7,
        dest_id=12,
        priority=Priority.NORMAL,
        payload=b"Lab results ready for collection"
    )
    message.ttl = 5

    print_packet(message, "💬")
    simulate_network_delay()

    # Node 3 receives and relays
    print_node(3, "Received packet for Node 12 (not for me)")
    print_node(3, "Relaying... (TTL=5 → 4)")
    message.ttl = 4
    print_packet(message, "↪️")
    simulate_network_delay()

    # Node 1 receives and relays
    print_node(1, "Received packet for Node 12 (not for me)")
    print_node(1, "Relaying... (TTL=4 → 3)")
    message.ttl = 3
    print_packet(message, "↪️")
    simulate_network_delay()

    # Node 5 receives and relays
    print_node(5, "Received packet for Node 12 (not for me)")
    print_node(5, "Relaying... (TTL=3 → 2)")
    message.ttl = 2
    print_packet(message, "↪️")
    simulate_network_delay()

    # Node 9 receives and relays
    print_node(9, "Received packet for Node 12 (not for me)")
    print_node(9, "Relaying... (TTL=2 → 1)")
    message.ttl = 1
    print_packet(message, "↪️")
    simulate_network_delay()

    # Node 12 receives final packet
    print_node(12, f"{Colors.GREEN}Received packet (for me!) - delivered!{Colors.END}")
    print_node(12, f"Message: '{message.payload.decode()}'")

    print(f"\n{Colors.GREEN}Result: Message routed through 4 hops to reach destination{Colors.END}")
    print(f"{Colors.CYAN}Path: 7 → 3 → 1 → 5 → 9 → 12{Colors.END}")

def interactive_menu():
    """Interactive demo menu"""
    print_header("RoamEN Interactive Demo")

    print(f"{Colors.BOLD}Welcome to the RoamEN protocol demonstration!{Colors.END}\n")
    print("This demo shows how RoamEN nodes communicate without actual radio hardware.\n")

    demos = [
        ("Network Beacons", demo_basic_beacon),
        ("Text Messaging", demo_text_message),
        ("Voice Transmission", demo_voice_transmission),
        ("Standard Alert", demo_alert_standard),
        ("Urgent Alert", demo_alert_urgent),
        ("Emergency Broadcast", demo_alert_emergency),
        ("IT Failure Scenario", demo_network_failure),
        ("Mesh Routing", demo_mesh_routing),
    ]

    while True:
        print(f"\n{Colors.BOLD}Choose a demo:{Colors.END}")
        print(f"  0. Run all demos")
        for i, (name, _) in enumerate(demos, 1):
            print(f"  {i}. {name}")
        print(f"  Q. Quit")

        choice = input(f"\n{Colors.BOLD}Enter choice: {Colors.END}").strip().upper()

        if choice == 'Q':
            print("\nThanks for trying RoamEN!")
            break
        elif choice == '0':
            for name, demo_func in demos:
                demo_func()
                input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.END}")
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(demos):
                    demos[idx][1]()
                    input(f"\n{Colors.CYAN}Press Enter to return to menu...{Colors.END}")
                else:
                    print(f"{Colors.RED}Invalid choice!{Colors.END}")
            except ValueError:
                print(f"{Colors.RED}Invalid choice!{Colors.END}")

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        # Run all demos non-interactively
        demos = [
            demo_basic_beacon,
            demo_text_message,
            demo_voice_transmission,
            demo_alert_standard,
            demo_alert_urgent,
            demo_alert_emergency,
            demo_network_failure,
            demo_mesh_routing,
        ]
        for demo in demos:
            demo()
            time.sleep(1)
    else:
        # Interactive mode
        interactive_menu()

if __name__ == "__main__":
    main()
