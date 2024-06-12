#! /usr/bin/env python3


def num_conv(i=1):
    """Convert 1 - 26 to alphabet character"""
    list_ = [chr(x) for x in range(97, 123)]
    return list_[i]


print(f"convertor_fun_only: __name__ == {__name__}")
