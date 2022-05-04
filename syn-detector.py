#!/usr/bin/env python3

from scapy.all import *
import sys
from collections import Counter
import seaborn as sns


def get_scanned_ports(pcap_fname, ip):
    portsScanned = []
    for pkt in PcapReader(pcap_fname):
        if pkt.haslayer(IP):
            if pkt.getlayer(IP).src == ip:
                portsScanned.append(pkt.getlayer(TCP).sport)
    return list(set(portsScanned))


def show_scanner_stats(scanner_dict):
    sns.set_theme(style="darkgrid")
    ax = sns.barplot(x=list(scanner_dict.keys()),
                     y=list(scanner_dict.values()))
    ax.set_xticklabels(list(scanner_dict.keys()), rotation=90)
    ax.set_title("Port Scan Detection")
    ax.set(xlabel='IP', ylabel='Number of ports scanned')
    plt.subplots_adjust(bottom=0.2)
    plt.show()


def main(pcap_fname):
    scanner_dict = {}
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
            scanned_ports = get_scanned_ports(pcap_fname, ip)
            scanner_dict[ip] = len(scanned_ports)
            print("Port scan conducted by IP:\n{}\nScanned ports:\n{}\n".format(
                ip, ", ".join(str(x) for x in scanned_ports)))

    show_scanner_stats(scanner_dict)


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Use: python syn-detector.py file.pcap')
        sys.exit(-1)
    main(sys.argv[1])
