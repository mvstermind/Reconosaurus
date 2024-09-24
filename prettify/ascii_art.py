import pyfiglet
from termcolor import colored


def display_name(target: str, recon_type: list[str]):
    f = pyfiglet.figlet_format("RECONOSAURUS", font="slant")
    colored_name = colored(f, "light_green")

    target_colored = colored(f"Target: {target}", "light_green")

    print()
    print(colored_name)
    print(target_colored)

    print(colored(f"Recon methods:", "light_green"), end="")
    for r_type in range(len(recon_type)):
        print(colored(recon_type[r_type], "light_green"), end=" ")

    print()


def pretty_print_result(): ...


# todo
