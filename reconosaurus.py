from datetime import datetime
from typing import Any

from arg_parser.arg_parser import parse_args
from bruteforce.dirs import read_wordlist_file_to_list
from bruteforce.port_scanner import scan_ports
from bruteforce.request import brute_force_with_dirs, wordlist_to_urls
from prettify import announcement, ascii_art


def main():
    # agrs fields: url ,wordlist, prefix, scan
    args = parse_args()
    if args.prefix:
        wordlist: list[str] = read_wordlist_file_to_list(
            path=args.wordlist, prefix=args.prefix
        )
    else:
        wordlist: list[str] = read_wordlist_file_to_list(path=args.wordlist)

    ascii_art.display_name(target=args.url, recon_type=args.type)

    # quirky way of finding all of recon types user picked. ik it's shitty
    for i in range(len(args.type)):

        # bruteforce url paths
        if args.type[i] == "dir":
            announcement.positive("-------------------------", end="")
            announcement.positive(f"Bruteforcing target: {args.url}")
            announcement.positive(f"Started at: {str(datetime.now())}")

            urls: list[str] = wordlist_to_urls(wordlist=wordlist, url=args.url)
            response_status: dict[str, int] = brute_force_with_dirs(
                urls=urls, max_workers=10
            )

        # port scanning
        elif args.type[i] == "port":
            ports = str(args.scan)
            print()
            announcement.positive("-------------------------", end="")
            announcement.positive(f"Scanning Target: {args.url}")
            announcement.positive(f"Started at: {str(datetime.now())}")

            open_ports: list[int] | None = []
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

    if args.save:
        save_results_to_file(response_status, open_ports, file=args.save)


def save_results_to_file(*output: Any, file: str) -> None:
    with open(file, "a") as f:
        for content in output:
            if isinstance(content, dict):
                for key, value in content.items():
                    f.write(f"{key} - {value}\n")
            else:
                f.write(str(content) + "\n")


if __name__ == "__main__":
    main()
