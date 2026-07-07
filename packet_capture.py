from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import threading

packets = []
capture_thread = None
is_capturing = False

def get_protocol(pkt):
    if pkt.haslayer(TCP):
        return "TCP"
    elif pkt.haslayer(UDP):
        return "UDP"
    elif pkt.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"

def process_packet(pkt):
    if pkt.haslayer(IP):
        record = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "src": pkt[IP].src,
            "dst": pkt[IP].dst,
            "protocol": get_protocol(pkt),
            "length": len(pkt),
            "info": ""
        }
        packets.append(record)

def start_sniffing():
    global is_capturing
    is_capturing = True
    sniff(prn=process_packet, store=False, stop_filter=lambda x: not is_capturing)

def start_capture():
    global capture_thread, packets, is_capturing
    packets = []
    capture_thread = threading.Thread(target=start_sniffing, daemon=True)
    capture_thread.start()

def stop_capture():
    global is_capturing
    is_capturing = False

def get_packets():
    return packets