#! /usr/bin/env python3


def print_values(**kwargs):
    print(type(kwargs), kwargs)
    for k, v in kwargs.items():
        print(f"{k.replace('_', ' ')}: {v}")


kwargs = {
    "first_name": "Tom",
    "sir_name": "Thumb",
    "age": "31",
    "address": "Kampala",
    "college": "Engineering",
}

print_values(**kwargs)

# End
