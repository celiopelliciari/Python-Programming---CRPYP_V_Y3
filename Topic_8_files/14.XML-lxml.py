#! /usr/bin/env python3

""" LXML module """

from lxml import etree

with open("show_security_zones.xml") as fh:

    # // Convert a string to an etree object //
    xml_sh_sec_zones = etree.fromstring(fh.read().strip())

# xml_sh_sec_zones = etree.parse("show_security_zones.xml").getroot()

print(dir(xml_sh_sec_zones))

print("\nTag: ", xml_sh_sec_zones.tag)

print("\n----\n")
print("\nget children: ", xml_sh_sec_zones.getchildren())
print("\nlist children: ", list(xml_sh_sec_zones))

print("\n----\n")
print("\nget children of child: ", xml_sh_sec_zones[0].getchildren())
print("\nlist children of child: ", list(xml_sh_sec_zones[0]))

print("\n----\n")
# // Find in the etree //
print("Root: ", xml_sh_sec_zones.find("."))
print("First zones-security: ", xml_sh_sec_zones.find("zones-security"))

print("All zones-security: ", xml_sh_sec_zones.findall("zones-security"))

print("\n----\n")
# // Find out what xpath notation is //
# // This means: Find the tag named 'zones-security-zonename' anywhere in the XML tree //
print(xml_sh_sec_zones.find(".//zones-security-zonename"))
print(xml_sh_sec_zones.find(".//zones-security-zonename").tag)
print(xml_sh_sec_zones.find(".//zones-security-zonename").text)

print("\n----\n")

print(xml_sh_sec_zones.findall(".//zones-security-zonename"))
print(xml_sh_sec_zones.findall(".//zones-security-zonename")[1].tag)
print(xml_sh_sec_zones.findall(".//zones-security-zonename")[1].text)

print("\n----\n")
# // Loop over immediate elements of the tree //
for child in xml_sh_sec_zones:
    print(child)

print("\n----\n")
# iterate over all the elements of the tree //
for child in xml_sh_sec_zones.iterdescendants():
    print(child)

print("\n----\n")
# // Convert the etree object to a byte string //
print(etree.tostring(xml_sh_sec_zones))

print("\n----\n")
# // Convert the etree object to a unicode string //
print(etree.tostring(xml_sh_sec_zones).decode())
