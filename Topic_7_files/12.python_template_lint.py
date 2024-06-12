#! /usr/bin/env python3
# -*- coding: utf-8 -*-

''' Program name and/or Documentation '''

# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys
import argparse

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

__author__ = "<AUTHOR NAME>"
__copyright__ = "Copyright <YEAR>, <INSTITUTION>"
__licence__ = "<LICENCE, i.e. European Union Public Licence v1.2>"
__version__ = "<VERSION OF PROGRAM>"
__program__ = sys.argv[0][2:] if (sys.argv[0][:2] == "./") else sys.argv[0]
OTHER = "OTHER GLOBAL DECLARATIONS HERE"

# ============================================ #
# //                Functions               // #
# ============================================ #

# -------------------------------------------- #
# //            other() Function            // #
# -------------------------------------------- #


def other(other_):
    """<OTHER>() function"""

    fun_name="<OTHER>()"
    return f"{fun_name}: {other_} STUFF HERE>"


## End <OTHER>() function

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #

def main(nspace):
    """main() function"""

    # // Print program name //
    print(__doc__)

    # // Arguments from shell //
    print(f"namespace: '{nspace}'")

    # // Arguments from shell as dictionary //
    print(f"dictionary: '{vars(nspace)}'")

    # // Arguments from shell
    print("main() action: 'print from main()'")

    ## // call <OTHER_FUNCTION>() //
    print('print from other()', other('OTHER'))    


# End main() function


# ============================================#
# //                  Global                //#
# ============================================#

# // Command line parsing //
parser = argparse.ArgumentParser(description="Description goes here")
parser.add_argument(
    "-a", '--arg_a', help="Argument A", nargs=1, type=ascii, required=False
)
parser.add_argument(
    "-b", '--arg_b', help="Argument B", nargs=2, type=int, required=False
)
parser.add_argument(
    "-c", '--arg_c', help="Argument C", nargs=1, type=float, required=False
)
parser.add_argument(
    "-d", '--arg_d', help="Argument D", action="store_true", required=False
)
parser.add_argument("other")

## // Call main function (Pick minimum version if necessary) //
if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor >= 0:
        main(parser.parse_args())
    else:
        print('A python version greater that 3.0 is required.')
else:
    sys.exit(1)
