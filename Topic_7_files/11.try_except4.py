#! /usr/bin/env python3

import sys

filename = "no_read_file.no"

try:
    fh = open(filename, mode="r")
    print(fh.read())
except FileNotFoundError as e:
    print(f"No such file: '{filename}'")
    print(f"Logging: {e}")
except PermissionError as e:
    print(f"Bad permissions to access: '{filename}'")
    print(f"Logging: {e}")
except Exception as e:
    print(f"New un-excepted Error")
    raise OSError(e)
finally:
    print("Do this if try succeeds or fails")

print("Moved on in program")

# End
