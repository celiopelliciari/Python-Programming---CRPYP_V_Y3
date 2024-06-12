#! /usr/bin/env python3

import sys

# Open file for writing
some_text = "Some more text"

# Writing to a file
fh = open("file.txt", mode="w", encoding="utf-8")
fh.write("This is a test file\nthat I want to write to")
fh.write("\n")
fh.write(some_text)
fh.write("\nfinished.")
fh.write("\n")
fh.close()

# // End //
sys.exit(0)
