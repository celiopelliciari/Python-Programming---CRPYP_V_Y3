#! /usr/bin/env python3

""" XML namespaces """

from lxml import etree
from pprint import pprint

# // Generate an etree ElementTree //
xml_sh_ver = etree.parse("show_version.xml")

# // Extract the etree root Element from the etree //
xml_sh_ver_root = xml_sh_ver.getroot()

print()
print("Element tree: ", xml_sh_ver)

print("\n ---- \n")
print("Element tree root : ", xml_sh_ver.getroot())

print("\n ---- \n")
print("Namespace map: ")
pprint(xml_sh_ver_root.nsmap)

print("\n ---- \n")
print("Element: ", xml_sh_ver_root[0])

print("\n ---- \n")
# // Access the text of the "chassis_id" element //
print("Chassis ID: ", end="")
print(xml_sh_ver_root.find(".//{*}chassis_id").text)

print("\n ---- \n")
