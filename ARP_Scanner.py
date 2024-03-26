# Credits for s4vitar in https://hack4u.io
#!/usr/bin/env python3

import sys
import signal
import argparse
import scapy.all as scapy
import textwrap
from termcolor import colored

def def_handler(sig, frame):
    print(colored("[!] Exit...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():

    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="ARP range to scan (Example: -t 172.16.0.111/24)")
    args = parser.parse_args()
    return args.target

def scan(ip):

    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast_packet / arp_packet
    answered, _ = scapy.srp(arp_packet, timeout=1, verbose=False)

    for i in answered:
        ip_address = i[1].psrc
        mac_address = i[1].hwsrc
        print_result(ip_address, mac_address)

def print_result(ip, mac):

    ip_width = 20
    mac_width = 17
    ip_formatted = textwrap.shorten(ip, width=ip_width)
    mac_formatted = textwrap.shorten(mac, width=mac_width)
    print(colored(f"[+] {ip_formatted.center(ip_width)} {mac_formatted.center(mac_width)}", 'green'))

def main():

    target = get_arguments()
    print(colored(f"{'IP Address'.center(20)} {'MAC Address'.center(17)}", 'cyan'))
    print("-" * 40)
    scan(target)

if __name__ == '__main__':
    main()
