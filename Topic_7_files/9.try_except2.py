#! /usr/bin/env python3

import sys

filename = "no_read_file.no"

try:
    fh = open(filename, mode="r")
    print(fh.read())
except FileNotFoundError as e:
    print(f"No such file: '{filename}'")
    print(f"Logging: {e}")
finally:
    print("Do this if try succeeds or fails")

print("Moved on in program")

# End
