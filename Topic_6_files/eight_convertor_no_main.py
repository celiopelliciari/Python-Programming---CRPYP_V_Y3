#! /usr/bin/env python3

import sys


def num_conv(i=1):
    """Convert 1 - 26 to alphabet character"""
    list_ = [chr(x) for x in range(97, 123)]
    return list_[i]


print(f"convertor_no_main: __name__ == {__name__}")
while True:
    i = input("Enter an integer (NO): ")
    i = int(i) if (i.isdigit()) else sys.exit(1)
    print(num_conv(i - 1).upper())
