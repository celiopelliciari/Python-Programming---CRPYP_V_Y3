#! /usr/bin/env python3
""" Yaml start """

import sys
import yaml

# Variables
file = "data.yaml"
file2 = "data2.yaml"


print()
# // Open a yaml file for reading //
with open(file, mode="r") as fh:
    head_ = fh.readline()
    yaml_in = yaml.load(fh, Loader=yaml.FullLoader)
    print(f"{type(yaml_in)}\n{yaml_in}")
    print()

print("\n---------------\n")

while True:
    input("Press 'Enter' to continue")
    print()

    # // Open a multi-doc yaml file for reading //
    with open(file2, mode="r") as fh:
        head_ = fh.readline()
        yaml_in2 = yaml.load_all(fh, Loader=yaml.FullLoader)
        print(type(yaml_in2), yaml_in2)
        for doc in yaml_in2:
            print(doc)
            print("\n---------------\n")
