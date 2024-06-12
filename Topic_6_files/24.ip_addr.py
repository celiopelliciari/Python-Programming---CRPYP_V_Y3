#! /usr/bin/env python3
""" IP address tester """

import ipaddress
import sys

helper = f"\nUsage: ~$ {sys.argv[0]} --ip | --net <IP address>\n"

if not (len(sys.argv) == 3):
    print(helper)
    sys.exit(1)

# // IP address //
if sys.argv[1].strip().lower() == "--ip":
    ip = sys.argv[2]
    try:
        ipaddress.ip_interface(ip).ip
        print(
            f"\nTrue:: {type(ipaddress.ip_interface(ip).ip)}",
            f" :: {str(ipaddress.ip_interface(ip).ip)}\n",
        )
    except:
        print("\nFalse:: This is not an IP address\n")
        sys.exit(1)
    sys.exit(0)

# // IP network //
if sys.argv[1].strip().lower() == "--net":
    ip = sys.argv[2]
    try:
        ipaddress.ip_network(ip)
        print(
            f"\nTrue:: {type(ipaddress.ip_network(ip))}",
            f" :: {ipaddress.ip_network(ip)}\n",
        )
    except:
        print("\nFalse:: This is not an IP network\n")
        sys.exit(1)
    sys.exit(0)

# // help //
else:
    print(helper)
    sys.exit(1)

# // End //
sys.exit(0)
