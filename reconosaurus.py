import ascii_art
from arg_parser.arg_parser import parse_args
from bruteforce.dirs import read_wordlist_file_to_list
from bruteforce.request import brute_force_with_dirs, wordlist_to_urls


def main():
    ascii_art.display_name()
    # agrs fields: url ,wordlist, prefix
    args = parse_args()
    if args.prefix:
        wordlist: list[str] = read_wordlist_file_to_list(
            path=args.wordlist, prefix=args.prefix
        )
    else:
        wordlist: list[str] = read_wordlist_file_to_list(path=args.wordlist)

    # valid "types", that means attack types are: dir, port
    match args.type:
        case "dir":
            urls: list[str] = wordlist_to_urls(wordlist=wordlist, url=args.url)
            valid_resp: dict[str, int] = brute_force_with_dirs(
                urls=urls, max_workers=10
            )
            print(valid_resp)
        case "port":
            ...


if __name__ == "__main__":
    main()
