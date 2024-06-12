#! /usr/bin/env python3


def the_a_square(x, y):
    z = (x + y) * (x + y)
    return z


the_b_square = lambda x, y: ((x + y) * (x + y))

print("A. ", the_a_square(5, 2))

print("B. ", the_b_square(5, 2))
