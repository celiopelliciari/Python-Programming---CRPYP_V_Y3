#! /usr/bin/env python3


def add_numbers(x=4, y=5, z=6):
    """Add numbers"""

    a = x + y
    b = x + z
    c = y + z

    return (a, b, c)


sums = add_numbers(1, 2)
print(type(sums), sums)

# End
