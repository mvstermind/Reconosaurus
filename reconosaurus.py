from datetime import date, datetime

from termcolor import colored

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
            announcement.positive(f"Bruteforcing target: {args.url}")
            announcement.positive(f"Started at: {str(datetime.now())}")

            urls: list[str] = wordlist_to_urls(wordlist=wordlist, url=args.url)
            response_dict_w_status: dict[str, int] = brute_force_with_dirs(
                urls=urls, max_workers=10
            )
            announcement.positive("Found paths:")
            for path in response_dict_w_status:
                announcement.positive(
                    f"{path} responded with: {response_dict_w_status[path]}", end=""
                )

        # port scanning
        elif args.type[i] == "port":
            ports_to_scan = str(args.scan)
            print()
            announcement.positive(f"Scanning Target: {args.url}")
            announcement.positive(f"Started at: {str(datetime.now())}")

            try:
                ports_to_scan = int(ports_to_scan)
                scan_ports(target=args.url, last_port=ports_to_scan)

            except ValueError:
                ports_to_scan = str(ports_to_scan)
                first_port, last_port = ports_to_scan.split("-")
                first_port, last_port = int(first_port), int(last_port)
                scan_ports(target=args.url, first_port=first_port, last_port=last_port)


if __name__ == "__main__":
    main()
