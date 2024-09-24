from termcolor import colored


def positive_announcment(message: str) -> None:
    """
    prints out green text
    """
    print(colored(message, "green"))


def negative_announcment(message: str) -> None:
    """
    prints out red text
    """
    print(colored(message, "red"))
