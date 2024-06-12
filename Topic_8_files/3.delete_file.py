#!/usr/bin/env python3

import os

directory = "my_directory"
file = "file.txt"

# // Delete a file //
if os.path.isfile(f"{directory}/{file}"):
    print(f"File ' {file}' exists")
    os.remove(f"{directory}/{file}")
    print(f"Deleted '{file}'")
