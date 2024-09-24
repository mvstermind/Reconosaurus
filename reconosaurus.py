from arg_parser.arg_parser import parse_args
from bruteforce.dirs import read_wordlist_file_to_list


def main():
    args = parse_args()
    print(f"URL: {args.url}")
    print(f"Wordlist: {args.wordlist}")
    print(f"Prefix: {args.prefix}")
    wordlist: list[str] = read_wordlist_file_to_list(
        path=args.wordlist, prefix=args.prefix
    )


if __name__ == "__main__":
    main()
