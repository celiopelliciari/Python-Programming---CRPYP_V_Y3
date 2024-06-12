#! /usr/bin/env python3

y = 3

for x in range(5):
    if x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} must not be less than {y} after all")
        raise ValueError(f"Program stopped as {x} == {y}")
else:
    print("This is never going to happen")

# End
