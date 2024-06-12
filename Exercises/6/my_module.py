#!/usr/bin/python3

"""
Modules in Python3
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

import math

# ============================================ #
# //                Functions               // #
# ============================================ #


# Product of Range between two numbers
# Accept any number of arguments and assemble them into a tuple
def range_prod(*args):
    r1, r2 = 0, 0
    # Check the length of the arguments tuple
    if len(args) == 1:
        r1, r2 = 1, args[0]
    elif len(args) > 1:
        r1, r2 = args[0], args[1]

    # Generate a list, called list_, which contains all the numbers between r1 and r2, including r2
    list_ = list(range(r1, r2 + 1))

    # Using the prod() function from the math module, get the product of all the
    # elements in the range. Call the result ans
    ans = math.prod(list_)

    # Return a tuple with the elements r1, r2 and ans
    return r1, r2, ans

# End range_prod(*args) function

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #


def main():
    # Define an integer variable, called default_variable, with a value of 5
    default_variable = 5

    # Call the range_prod():, with default_variable as an argument
    # Trap the tuple elements returned as a, b, c
    a, b, c = range_prod(default_variable)

    # Print the result to the terminal in the form “MOD: The product of the
    # range from a .. b = c”
    print(f"MOD: The product of the range from {a} .. {b} = {c}")

# End main() function


# // Call main function //
if __name__ == "__main__":
    main()
