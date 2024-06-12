#! /usr/bin/env python3

"""  Exercise #6.1 in Python3  """


def my_function(required, *args, **kwargs):
    """My Function"""

    # // Print the required variable type and value //
    print(type(required), f"{required}\n")

    # // Print additional variable types and values received //
    if args:
        print(type(args), args, "\n")

    # // Print the key/values type and data received //
    if kwargs:
        print(type(kwargs), kwargs, "\n")

    # // Return a list including all the data received //
    return [required, args, kwargs]


# // Assign the returned data to a list, list_ //
list_ = my_function("1", 2, 3, 4, a=1, b=2, c=3, d=4)

# // Loop through list_ and print out each element.
for x in list_:
    print(f"{x}\n")
