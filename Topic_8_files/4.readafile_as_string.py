#! /usr/bin/env python3

import sys

# // File for reading //
file = "unstructured_data.txt"

print()

# // Read entire file //
print("** Reading entire file, this is the output **\n")
fh = open(file, mode="r")
print((type(fh), fh))
entire_file = fh.read()
print(entire_file)
print()

# // Closing filehandle //
fh.close()

# // Read entire file (alternative format) //
print()
print("** Reading entire file, this is the output **\n")
with open(file) as fh2:
    print((type(fh2), fh2))
    entire_file2 = fh2.read()

print(entire_file2)

try:
    entire_file3 = fh2.read()
except:
    print("\nfilehandle 'fh2' was closed with the indent closure\n")

print("** splitlines() for some structure **\n")
structured_list = entire_file.splitlines()
print(structured_list)

# // End //
sys.exit(0)
