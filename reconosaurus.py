"""
Main file of the program
"""

from datetime import datetime

import save_output as save
from arg_parser.arg_parser import parse_args
from bruteforce import cms, os_detection
from bruteforce.dirs import read_wordlist_file
from bruteforce.port_scanner import scan_ports
from bruteforce.request import brute_force_w_dir, wordlist_to_urls
from prettify import ascii_art, colorify

open_ports: list[int] | None = []


def main():
    # agrs fields: url ,wordlist, prefix, scan
    args = parse_args()
    if args.prefix:
        wordlist: list[str] = read_wordlist_file(path=args.wordlist, prefix=args.prefix)
    else:
        wordlist: list[str] = read_wordlist_file(path=args.wordlist)

    ascii_art.display_name(target=args.url, recon_type=args.type)

    # initalize variables, in case of writing to a file so it won't crash
    response_status, open_ports, cms_detected = None, None, None

    # quirky way of finding all of recon types user picked. ik it's shitty
    for i in range(len(args.type)):

        # bruteforce url paths
        if args.type[i] == "dir":
            colorify.positive("-------------------------", end="")
            colorify.positive(f"Bruteforcing target: {args.url}")
            colorify.positive(f"Started at: {str(datetime.now())}")

            urls: list[str] = wordlist_to_urls(wordlist=wordlist, url=args.url)
            response_status: dict[str, int] = brute_force_w_dir(
                urls=urls, max_workers=10
            )

        # port scanning
        elif args.type[i] == "port":
            ports = str(args.scan)
            print()
            colorify.positive("-------------------------", end="")
            colorify.positive(f"Scanning Ports: {args.url}")
            colorify.positive(f"Started at: {str(datetime.now())}")

            try:
                ports = int(ports)
                open_ports = scan_ports(target=args.url, last=ports)

            except ValueError:
                ports = str(ports)
                first_port, last_port = ports.split("-")
                first_port, last_port = int(first_port), int(last_port)
                open_ports = scan_ports(
                    target=args.url, first=first_port, last=last_port
                )

        elif args.type[i] == "cms":
            colorify.positive("-------------------------", end="")
            colorify.positive(f"Scanning {args.url} for CMS")
            cms_detected: str = cms.detect(url=args.url)

        elif args.os and args.ports:
            colorify.positive("Performing ICMP Ping...")
            os_detection.icmp_ping(args.url)

            os_port: int = 0
            try:
                os_port = int(args.ports)
                colorify.positive("Performing TCP SYN Scan...")
                os_detection.syn_probe_multiple_ports(args.url, [1, os_port])

            except ValueError:
                str_port = str(os_port)
                first_port, last_port = str_port.split("-")
                first_port, last_port = int(first_port), int(last_port)
                colorify.positive("Performing TCP SYN Scan...")
                os_detection.syn_probe_multiple_ports(args.url, [first_port, last_port])

    if args.save:
        save.results_to_file(response_status, open_ports, cms_detected, file=args.save)


if __name__ == "__main__":
    main()
