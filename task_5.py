from scapy.all import sniff, IP, TCP, UDP, ICMP

def process_packet(packet):
    """Process and display details of a captured packet."""
    print("\n--- Packet Captured ---")
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
    else:
        print("Packet does not contain IP layer.")
    if TCP in packet:
        print("Protocol: TCP")
        print(f"Source Port: {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
    elif UDP in packet:
        print("Protocol: UDP")
        print(f"Source Port: {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")
    elif ICMP in packet:
        print("Protocol: ICMP")
        print(f"Type: {packet[ICMP].type}")
        print(f"Code: {packet[ICMP].code}")
    else:
        print("Protocol: Other")
    if packet.haslayer("Raw"):
        payload = packet["Raw"].load
        print(f"Payload: {payload}")
    else:
        print("No payload data available.")

def main():
    print("Starting packet sniffer...")
    print("Press Ctrl+C to stop.")
    try:
        sniff(filter="ip", prn=process_packet, count=100)
    except KeyboardInterrupt:
        print("\nPacket sniffing stopped by user.")
    except PermissionError:
        print("\nError: You need to run this script as root/administrator.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
