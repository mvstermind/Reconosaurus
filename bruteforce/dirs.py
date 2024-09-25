"""
Opens, reads and returns a list[str] of all words from given file
"""

import sys

from prettify import colorify


def read_wordlist_file(path: str, prefix: str = "") -> list[str]:
    """
    Reads given file
    Extracts all of the data from it and turns it into list[str]
    path: str -> path to wordlist
    prefix: str (optional) -> adds given prefix at the end of word from wordlist


    returns: list[str] -> all of words that were found inside file with
    optionally defined prefix

    if path doesn't exist or is invalid
    it exits a program
    """
    try:
        dirs: list[str] = []
        with open(path, "r") as file:
            for line in file:

                if prefix != "":
                    prefix = prefix.strip()
                    line = line.strip()

                    if "." in line:
                        continue
                    else:
                        line += prefix

                else:
                    line = line.strip()
                dirs.append(line)
        return dirs
    except Exception:
        colorify.negative(f"'{path}' is not valid path")
        sys.exit()
