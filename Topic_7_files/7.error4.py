#! /usr/bin/env python3

import os

y = 3

for x in range(5):
    if x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{c} must not be less than {y} after all")
        os._exit(1)
else:
    print("This is never going to happen")

# End
