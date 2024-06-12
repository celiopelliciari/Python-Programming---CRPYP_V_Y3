#! /usr/bin/env python3

""" The built-in eval() function """

str_ = "some_fun"


def some_fun(*args):
    """function to sum all the values given"""

    s = sum(list(args))
    return s


# // Main section //

print(some_fun(1, 2, 3, 4))

print(
    f"As expected, how about replacing the ",
    f"function name with a string that is  ",
    f"the function name?\n",
)

try:
    f"{str_}"(1, 2, 3, 4)

except TypeError:
    print("Ooops: 'str' object is not callable\n")

# print('Make the lot into a string: ', f"{str_}({*list_})'")

print(f"{str_}(1,2,3,4)\n")

print("Evaluate the string:", eval(f"{str_}(1,2,3,4)"))
