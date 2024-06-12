#! /usr/bin/env python3


def add_numbers(*args):
    x = args[0]
    y = args[1]
    z = args[2]
    a = x + y
    b = x + z
    c = y + z
    return (a, b, c)


args = (1, 2, 3)
sums = add_numbers(*args)
print(type(sums), sums)

# End
