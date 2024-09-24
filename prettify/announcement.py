"""
Used to print out messages to stdout but with colors
"""

from termcolor import colored


def positive(message: str, end="\n") -> None:
    """
    prints out green text
    message: str - content to print in color
    end: str - defines what should be printed at the end of the line
    default is '\n'
    """
    print()
    print(colored(message, "light_green"), end=end)


def negative(message: str, end="\n") -> None:
    """
    prints out red text
    message: str - content to print in color
    end: str - defines what should be printed at the end of the line
    default is '\n'
    """
    print(colored(message, "red"), end=end)
