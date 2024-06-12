#!/usr/bin/env python3

""" Colour map module """

import sys

print(f"\nColour map module: {__name__}")

colours = {
    "Black": "\033[0;30m", "Dark Gray": "\033[1;30m",
    "Blue": "\033[0;34m", "Light Blue": "\033[1;34m",
    "Green": "\033[0;32m", "Light Green": "\033[1;32m",
    "Cyan": "\033[0;36m", "Light Cyan": "\033[1;36m",
    "Red": "\033[0;31m", "Light Red": "\033[1;31m",
    "Purple": "\033[0;35m", "Light Purple": "\033[1;35m",
    "Brown": "\033[0;33m", "Yellow": "\033[1;33m",
    "Light Gray": "\033[0;37m", "White": "\033[1;37m",
    "Reset": "\033[0;0m", "Bold": "\033[;1m",
    "Reverse": "\033[;7m", "Underline": "\033[04m",
    "Strikethru": "\033[09m", "Invisible": "\033[08m",
}

# // End //
