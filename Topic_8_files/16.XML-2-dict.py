#! /usr/bin/env python3

""" XML to Dictionary """

# // Install: python3 -m pip install xmltodict

import xmltodict

# // Read the XML file as a etree //
with open("show_security_zones.xml") as fh:
    sh_sec = fh.read().strip()

sh_sec_etree = xmltodict.parse(sh_sec)

print("\n ---- Ordered Dictionary ---- \n")
print(type(sh_sec_etree))
# // Print out this new variable and its type //
print(sh_sec_etree)

print("\n ---- Extracting data ---- \n")
zones_security = sh_sec_etree["zones-information"]["zones-security"]
for c, x in enumerate(zones_security):
    print(f"Security Zone #{c + 1}: {x['zones-security-zonename']}")

print("\n ---- Regular Dictionary instead of Ordered Dictionary ---- \n")
sh_sec_etree = xmltodict.parse(sh_sec, dict_constructor=dict)

print(sh_sec_etree)
