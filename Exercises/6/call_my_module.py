#!/usr/bin/python3

"""
Call modules in Python3
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

# mport the my_module module
import my_module

# ============================================ #
# //                  Global                // #
# ============================================ #

# Define a list, called list_, that contains five tuples
# The first tuple should only contain one element, the integer 5
# The remaining tuples should contain two integers, 2,5; 3,5; 4,5 and 5,5
list_ = [(5,), (2, 5), (3, 5), (4, 5), (5, 5)]

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #


def main():
    # Loop through the tuples in the list, list_
    for i in list_:
        # Send each tuple to the range_prod() function in the my_module for processing
        # Trap the returned tuple as x, y, z
        x, y, z = my_module.range_prod(*i)

        # Print the result to the terminal in the form “CALL: The product of the
        # range from x .. y = z”
        print(f"CALL: The product of the range from {x} .. {y} = {z}")

# End main() function


# // Call main function //
if __name__ == "__main__":
    main()
