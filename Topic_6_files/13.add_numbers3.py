#! /usr/bin/env python3


def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    return (a, b, c)


args = (1, 2, 3)
sums = add_numbers(*args)
print(type(sums), sums)

# End
