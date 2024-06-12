#! /usr/bin/env python3


def print_values(**kwargs):
    print(type(kwargs), kwargs)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print_values(first_name="Tom", 
             sir_name="Thumb", 
             age="31")

# End
