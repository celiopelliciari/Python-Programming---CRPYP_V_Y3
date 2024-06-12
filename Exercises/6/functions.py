#!/usr/bin/python3

"""
Functions in Python3

    This function takes a required variable, additional positional arguments, and keyword arguments.
    It prints the types and values of received variables and returns them as a list.

    Parameters:
    required_var: The required variable.
    *args: Additional positional arguments.
    **kwargs: Additional keyword arguments.

    Returns:
    A list including all the data received.
"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

from sys import argv

# ============================================ #
# //                Functions               // #
# ============================================ #


def my_function(required_var, *args, **kwargs):

    # Print the required variable type and value received
    print(f"Required variable type: {type(required_var)}. Required variable value: {required_var}")

    # Print any additional variable types and values received
    if args:
        for arg in args:
            print(f"Additional variable type: {type(arg)}. Additional variable value: {arg}.")

    # Print the key/values type and data received
    if kwargs:
        for key, value in kwargs.items():
            print(f"Additional variable key type: {type(key)}, value type: {type(value)}. "
                  f"Key: {key}, value: {value}.")

    # Return a list including all the data received
    return [required_var] + list(args) + list(kwargs.items())

# End my_function() function

# -------------------------------------------- #
# //            main() Function             // #
# -------------------------------------------- #


def main():

    # Checking if user has provided the “required” variable
    if len(argv) <= 1:
        print("Error: You need to provide at least one variable.")
        exit(1)  # Exit with an error code

    # Extract positional arguments (if any)
    positional_args = argv[2:]

    # Sorting out keyword arguments from remaining arguments
    keyword_args = {}
    for arg in positional_args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            keyword_args[key] = value
            positional_args.remove(arg)

    # Assign the returned data to a list, list_
    list_ = my_function(argv[1], *positional_args, **keyword_args)

    # Loop through the list, list_ and print out each element
    for item in list_:
        print(item)

# End main() function


# // Call main function //
if __name__ == "__main__":
    main()
