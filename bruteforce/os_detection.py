from typing import List, Optional

from scapy.all import ICMP, IP, TCP, Packet, sr, sr1

import prettify
from prettify import colorify


def syn_probe(dst_ip: str, dst_port: int) -> None:
    """
    Sends a TCP SYN probe to the specified destination IP and port, and prints the analysis of the response.
    :param dst_ip: Destination IP address as a string.
    :param dst_port: Destination port as an integer.
    :return: None
    """
    syn_pkt: IP = IP(dst=dst_ip) / TCP(dport=dst_port, flags="S")

    # Send the packet and wait for a response (timeout set to 5 seconds)
    resp: Optional[Packet] = sr1(syn_pkt, timeout=5)

    if resp is None:
        print(
            f"No response from {dst_ip} on port {dst_port} (likely filtered or no service)"
        )
    elif resp.haslayer(TCP):
        tcp_resp = resp.getlayer(TCP)
        if tcp_resp.flags == "SA":
            print(f"SYN-ACK received from {dst_ip} - Port {dst_port} is open")
        elif tcp_resp.flags == "RA":
            print(f"RST-ACK received from {dst_ip} - Port {dst_port} is closed")
    else:
        print("Unexpected response received")


def syn_probe_multiple_ports(dst_ip: str, ports: List[int]) -> None:
    """
    Scans multiple ports on a destination IP using TCP SYN probes.
    :param dst_ip: Destination IP address as a string.
    :param ports: List of ports to scan as integers.
    :return: None
    """
    for port in ports:
        colorify.positive(f"Scanning port {port} on {dst_ip}...")
        syn_probe(dst_ip, port)


def syn_probe_with_sr(dst_ip: str, dst_port: int) -> None:
    """
    Uses sr() to send a TCP SYN probe and get more detailed responses.
    :param dst_ip: Destination IP address as a string.
    :param dst_port: Destination port as an integer.
    :return: None
    """
    syn_pkt: IP = IP(dst=dst_ip) / TCP(dport=dst_port, flags="S")
    ans, unans = sr(syn_pkt, timeout=5)

    if ans:
        for sent, received in ans:
            if received.haslayer(TCP):
                tcp_resp = received.getlayer(TCP)
                if tcp_resp.flags == "SA":
                    colorify.positive(
                        f"SYN-ACK received from {dst_ip} - Port {dst_port} is open"
                    )
                elif tcp_resp.flags == "RA":
                    colorify.negative(
                        f"RST-ACK received from {dst_ip} - Port {dst_port} is closed"
                    )
    else:
        colorify.negative(
            f"No response from {dst_ip} on port {dst_port} (likely filtered)"
        )


def icmp_ping(dst_ip: str) -> None:
    """
    Sends an ICMP echo request (ping) to check if the host is up.
    :param dst_ip: Destination IP address as a string.
    :return: None
    """
    icmp_pkt: IP = IP(dst=dst_ip) / ICMP()
    resp: Optional[Packet] = sr1(icmp_pkt, timeout=3)

    if resp is None:
        colorify.negative(
            f"No ICMP response from {dst_ip} (host might be down or ICMP blocked)"
        )
    else:
        colorify.positive(f"ICMP response from {dst_ip} (host is up)")


if __name__ == "__main__":
    target_ip = "127.0.0.1"
    ports_to_scan = [80, 443, 22, 8080]

    colorify.positive("Performing ICMP Ping...")
    icmp_ping(target_ip)

    print("\nPerforming TCP SYN Scan...")
    syn_probe_multiple_ports(target_ip, ports_to_scan)
