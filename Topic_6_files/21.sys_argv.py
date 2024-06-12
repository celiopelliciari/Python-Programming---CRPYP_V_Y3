#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# // Command line parsing //
print(sys.argv)

print(f"Program name: {sys.argv[0]}")
for (c, x) in enumerate(sys.argv[1:]):
    print(f"Argument #{c + 1}: {x}")
print()
