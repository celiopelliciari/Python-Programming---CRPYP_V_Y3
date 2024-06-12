#!/usr/bin/env python3

""" Colour text """

from three_colour_map import colours as cm

import sys

# // Print module name //

print(f"{sys.argv[0][2:]}: {__name__}\n")

# // Print coloured text //

for x in list(cm.keys())[:-6]:
    print(f"{cm[x]}Text colour")

print(f"{cm['Reset']}\nText colour reset\n")

for x in list(cm.keys())[:-6]:
    print(f"{cm[x]}{cm['Underline']}Text colour underline")

print(f"{cm['Reset']}\nText colour reset\n")

for x in list(cm.keys())[:-6]:
    print(f"{cm[x]}{cm['Strikethru']}Text colour strikethrough")

print(f"{cm['Reset']}\nText colour reset\n")

print(f"{cm['Invisible']}Text colour {cm['Reset']}with invisible part")

print(f"{cm['Reset']}\nText colour reset\n")

# // End //
