import pyfiglet
from termcolor import colored


def display_name():
    f = pyfiglet.figlet_format("RECONOSAURUS", font="slant")
    colored_name = colored(f, "light_green")
    print()
    print(colored_name)


if __name__ == "__main__":
    display_name()
