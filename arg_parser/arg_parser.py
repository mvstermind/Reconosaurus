"""
Reads all of command line arguments
"""

import argparse


def parse_args() -> argparse.Namespace:
    """
    Reads argument from command line interface and returns thier value
    Required: "--url", "--type"
    Optional: "--wordlist", "--prefix", "--scan", "--save"
    """

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="Reconasaurus",
        description="Reconasaurus: The ultimate beast for brute-forcing directories, scanning ports, and hunting for vulnerabilities. Whether you're searching for hidden files, sniffing out open services, or identifying subdomains, Reconasaurus stomps through it all with prehistoric power!",
        epilog="Unleash the dino-might with Reconasaurus! Remember: With great power comes great recon... and maybe some ethical pwnage!",
    )

    # required positional argument
    recon_options: list[str] = ["dir", "port"]
    parser.add_argument(
        "-t",
        "--type",
        help=f"Type of operation to pefrorm",
        choices=recon_options,
        required=True,
        nargs="*",
    )

    parser.add_argument(
        "-u",
        "--url",
        help="URL to perform attack on",
        required=True,
    )

    # optional arguments
    parser.add_argument(
        "-w",
        "--wordlist",
        help="Directory of wordlist to use for performing dir bruteforce",
        default="./lists/dir-list.txt",
    )

    parser.add_argument(
        "--prefix",
        help="Add file prefix to wordlists bruteforce",
        required=False,
    )

    parser.add_argument(
        "--scan",
        help="Specify range of ports, or single port to perform scan on",
        required=False,
        default=1024,
        type=str,
    )

    parser.add_argument(
        "--save",
        help="Save result to given file",
        required=False,
    )

    args: argparse.Namespace = parser.parse_args()
    return args
