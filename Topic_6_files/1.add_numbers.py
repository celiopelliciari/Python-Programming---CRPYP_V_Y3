#! /usr/bin/env python3


def add_numbers(x, y, z):
    """Add numbers"""

    a = x + y
    b = x + z
    c = y + z

    return (a, b, c)


sums = add_numbers(1, 2, 3)
print(type(sums), sums)

# End
