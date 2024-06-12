#! /usr/bin/env python3


def add_numbers(x, y, z) -> tuple:
    """Add Numbers with annotate"""

    a = x + y
    b = x + z
    c = y + z

    return (a, b, c)


sums = add_numbers(1, 2, 3)
print(type(sums), sums)

print(add_numbers.__annotations__)

print(add_numbers.__annotations__["return"])

# End
