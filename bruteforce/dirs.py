def read_wordlist_file_to_list(path: str, prefix: str = "") -> list[str]:
    """
    Reads wordlist file given through cli
    And extracts all of the data from it
    """
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
