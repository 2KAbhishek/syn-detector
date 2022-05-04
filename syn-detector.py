#!/usr/bin/env python3

from scapy.all import *
import sys
from collections import Counter


def main(pcap_fname):
    syn_ip_list = []
    syn_ack_ip_list = []

    for pkt in PcapReader(pcap_fname):
        if pkt.haslayer(TCP):
            if pkt.getlayer(TCP).flags == 2:
                syn_ip_list.append(pkt.getlayer(IP).src)
            if pkt.getlayer(TCP).flags == 18:
                syn_ack_ip_list.append(pkt.getlayer(IP).dst)

    syn_counts = Counter(syn_ip_list)
    syn_ack_counts = Counter(syn_ack_ip_list)

    for ip in syn_counts:
        if syn_counts[ip] > 3 * syn_ack_counts[ip]:
            print(ip)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Use: python syn-detector.py file.pcap')
        sys.exit(-1)
    main(sys.argv[1])
