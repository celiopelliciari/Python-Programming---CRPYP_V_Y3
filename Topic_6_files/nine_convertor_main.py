#! /usr/bin/env python3

import sys


def num_conv(i=1):
    """Convert 1 - 26 to alphabet character"""
    list_ = [chr(x) for x in range(97, 123)]
    return list_[i]


def main():
    """Main function"""
    while True:
        i = input("Enter an integer (MA): ")
        i = int(i) if (i.isdigit()) else sys.exit(1)
        print(num_conv(i - 1).upper())


print(f"convertor_main: __name__ == {__name__}")
if __name__ == "__main__":
    main()
