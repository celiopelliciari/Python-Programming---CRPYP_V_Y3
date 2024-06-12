#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exercise #6.2 - pinger2 """

# ============================================ #
# //             Module imports             // #
# ============================================ #

import ipaddress
import sys
import subprocess as sp
import argparse as ap

# ============================================ #
# //           Dunder declarations          // #
# ============================================ #

__author__ = "Diarmuid O'Briain"
__copyright__ = "Copyright 2021, Institute of Technology Carlow"
__licence__ = "European Union Public Licence v1.2"
__version__ = "v1.0"
__program__ = sys.argv[0][2:] if (sys.argv[0][:2] == "./") else sys.argv[0]

# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //            licence() Function          // #
# -------------------------------------------- #


def licence(err_code=0):
    """Method to provide licence information"""

    print(f"\nAuthor    : {__author__}")
    print(f"Copyright : {__copyright__}")
    print(f"Licence   : {__licence__}\n")
    sys.exit(err_code)


# End licence() function

# -------------------------------------------- #
# //             ping() Function            // #
# -------------------------------------------- #


def ping(ipaddr):
    """ping() function"""

    try:
        ip = str(ipaddress.ip_interface(ipaddr).ip)
        p = sp.run(["ping", "-c", "1", ip], stdout=sp.PIPE)
        p = p.stdout.decode("utf-8")
    except Exception:
        err = f"{ipaddr} - ERROR: is not a properly formatted address"
        return err

    if "0 received" in p:
        ans = f"{ip} is unreachable"
    else:
        ans = f"{ip} is alive"
    return ans


# End ping() function

# -------------------------------------------- #
# //             main() Function            // #
# -------------------------------------------- #


def main(parse_args):
    """main() function"""

    # // call licence() //
    if parse_args.licence:
        licence()

    # // __call version__ //
    if parse_args.version:
        print(f"\nVersion: {__version__}\n")
        sys.exit(0)

    # // ping IP addresses //
    print()
    if len(parse_args.ip) > 0:
        for ip in parse_args.ip:
            print(f"{ping(ip)}")
    else:
        ip = input("Enter an IP address: ")
        print(f"{ping(ip)}")
    print()
    sys.exit(0)


# End main() function

# ============================================ #
# //           Global environment           // #
# ============================================ #


# // Command line parsing //
parser = ap.ArgumentParser(description=f"{__program__} IP address pinger program")
parser.add_argument(
    "-l",
    "--licence",
    "--license",
    help=f"{__program__} licence information",
    action="store_true",
    required=False,
)
parser.add_argument(
    "-v",
    "--version",
    help=f"{__program__} version information",
    action="store_true",
    required=False,
)
parser.add_argument(
    "-i", "--ip", default=[], help="IP address list", nargs="*", required=False
)

# // Call main function (Pick minimum version if necessary) //
if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor > 5:
        main(parser.parse_args())
    else:
        print("A python version greater that 3.5 is required.")
else:
    sys.exit(1)
