"""
Module that's only purpose is to get content and write it to file
"""

import sys
from typing import Any

from prettify import colorify


def results_to_file(*output: Any, file: str, save_mode: str = "a") -> None:
    """
    Saves any given data to a file, if not provided with save_mode,
    data will be appended to a file by default

    *output: Any -> any given output from user to be stored insde a file
    file: str -> file to write all of the given content to
    save_mode: str -> mode to use to modify file
    (accepts any valid that works
    with open() )

    if cannot write to a file, it will kill whole program.
    """
    try:
        with open(file, save_mode) as f:
            for content in output:
                if isinstance(content, dict):
                    for key, value in content.items():
                        f.write(f"{key} - {value}\n")
                else:
                    f.write(str(content) + "\n")

    except Exception:
        colorify.negative(f"Cannot use '{save_mode}' as valid mode for modyfing a file")
        sys.exit()
