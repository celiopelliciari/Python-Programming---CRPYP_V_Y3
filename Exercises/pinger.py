#!/usr/bin/python3

from subprocess import run, TimeoutExpired, CalledProcessError
from ipaddress import ip_address


def validate_ip(ip):
    """
    Validates IP address format and presence of malicious characters.
    """

    if not ip_address(ip) or any(char in ip for char in """`~!@#$%^&*()_-+=|\/:;"'<,>?{}[]|"""):
        raise ValueError
    else:
        return True


def ping_host(ip):
    """
    Pings once the specified IP address.
    """
    try:
        output = run(['ping', '-c', '1', ip], capture_output=True, text=True, check=True).stdout
        print("\n" + output + "\n" + f"{ip} is alive.")
    except TimeoutExpired:
        raise TimeoutError
    except CalledProcessError:
        raise CalledProcessError


def main():
    ip = input("Enter an IP address: ")
    if validate_ip(ip):
        ping_host(ip)


if __name__ == "__main__":
    main()
