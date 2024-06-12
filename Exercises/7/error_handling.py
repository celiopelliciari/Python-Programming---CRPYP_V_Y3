#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Error Handling in Python3"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #
"""Generate the following tuple ('1', 2, 3, '4', 'A', 5, 6, '7')"""
_tuple = ('1', 2, 3, '4', 'A', 5, 6, '7')

# ============================================ #
# //                Functions               // #
# ============================================ #

"""Create loop that prints the type and value of each element in the tuple. The
print() statement should be ended with end = ‘’ to prevent the default carriage
return."""


# START print_tuple()
def print_tuple(_tuple):
    for item in _tuple:
        print(f"{type(item)}, {item}. ", end='')
    print("\n")
# END print_tuple()


"""Add a try/except error handling mechanism to try and assign a converted
version of each element to an integer in a new variable. If successful print the
type and value of and should it fail except with a ValueError saying that that
particular element cannot be converted."""


# START error_handling()
def error_handling(_tuple):
    for item in _tuple:
        try:
            converted_value = int(item)
            print(f"{type(item)}, {item} now {type(converted_value)}, {converted_value}")
        except ValueError:
            print(f"{type(item)}, {item} now cannot be converted to an integer")
    print("\n")
# END error_handling()


"""Create an additional loop of the elements in the tuple, this time without the
try/except error handler. Assign the converted element to an integer and print
the type and element value to the screen. This will result in an error when the
loop gets to a non digit."""


# START convert()
def convert(_tuple):
    for item in _tuple:
        converted_value = int(item)
        print(type(converted_value), item, "now", type(converted_value), converted_value)
# END convert()


# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #


def main():
    print_tuple(_tuple)
    error_handling(_tuple)
    convert(_tuple)


if __name__ == "__main__":
    main()
else:
    sys.exit(1)
