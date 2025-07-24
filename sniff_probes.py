from scapy.all import *
import argparse

def sniff_probes(interface):
    def sniff_packet(packet):
        if packet.haslayer(Dot11ProbeReq):
            mac = packet.addr2
            ssid = packet.info.decode(errors='ignore')
            print(f"[+] Device {mac} is probing for SSID: {ssid}")
    sniff(iface=interface, prn=sniff_packet, store=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wi-Fi Probe Request Sniffer")
    parser.add_argument("-i", "--interface", help="Wireless interface in monitor mode", required=True)
    args = parser.parse_args()
    sniff_probes(args.interface)
