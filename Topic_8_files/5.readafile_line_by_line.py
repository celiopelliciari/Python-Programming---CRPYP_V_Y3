#! /usr/bin/env python3

import sys
from pprint import pprint

# // File for reading //
file = "unstructured_data.txt"
structured_list = list()

print()

# // Read unstructured data file line by line to list //
with open(file) as fh2:
    entire_file_as_list = fh2.readlines()

# // Output less-structured data //
print(type(entire_file_as_list), entire_file_as_list)

# // Process data in list //
for line in entire_file_as_list:
    structured_list.append(line.strip().split())

# // Output structured data //
print()
pprint(structured_list)

# // End //
sys.exit(0)
