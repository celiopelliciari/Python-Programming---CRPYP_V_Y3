#! /usr/bin/env python3

import sys

import seven_convertor_fun_only as conv
# import eight_convertor_no_main as conv
# import nine_convertor_main as conv


def main():
    while True:
        i = input("Enter an integer (AC): ")
        i = int(i) if (i.isdigit()) else sys.exit(1)
        print(conv.num_conv(i - 1).upper())


print(f"convertor_access: __name__ == {__name__}")
if __name__ == "__main__":
    main()
