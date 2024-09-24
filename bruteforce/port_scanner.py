import socket
import sys

from termcolor import colored


def scan_ports(target: str, first_port=1, last_port=1024) -> list[int] | None:
    """
    Scans for open prots using given parameters
    target: str -> IP address/url of tararget
    first_port: int -> first port to start scan on
    last_port: int -> last port to scan

    returns list[int] if everything went well, except error, then it just exits
    """

    open_ports: list[int] = []
    try:
        # scan every port
        for port in range(first_port, last_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            # append open ports to "open_ports"
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(result)
            s.close()

        return open_ports

    except KeyboardInterrupt:
        print(colored("\n Exitting...", "red"))
        sys.exit()

    except socket.error:
        print(colored("\n Host not responding", "red"))
