"""
Scans port a.k.a poor's man nmap
"""

import socket
import sys

from prettify import announcement


def scan_ports(target: str, first=1, last=1024) -> list[int] | None:
    """
    Scans for open prots using given parameters
    target: str -> IP address/url of tararget
    first_port: int -> first port to start scan on
    last_port: int -> last port to scan

    returns list[int] if everything went well, except error, then it just exits

    if KeyboardInterrupt or socket.error happens it will kill whole program
    """

    open_ports: list[int] = []
    try:
        # scan every port
        for port in range(first, last):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            # append open ports to "open_ports"
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(result)
            s.close()

        return open_ports

    except KeyboardInterrupt:
        announcement.negative("\nExiting")
        sys.exit()

    except socket.error:
        announcement.negative("\nHost is not responding...")
        sys.exit()
