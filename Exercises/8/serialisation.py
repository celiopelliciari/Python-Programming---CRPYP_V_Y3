#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Serialisation in Python3"""

# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys
import yaml
import json
from pprint import pprint

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

input_file = "network.yaml"
output_file = "network.json"

# ============================================ #
# //                Functions               // #
# ============================================ #


# START open_print_yaml()
def open_print_yaml():
    print(f"Reading the {input_file} YAML file")
    with open(input_file, mode="r") as fh:
        data = yaml.load(fh, Loader=yaml.SafeLoader)
    print(f"ens192: {data['network']['ethernets']['ens192']['addresses']}")
    print(f"ens224: {data['network']['ethernets']['ens224']['addresses']}")
    return data
# END open_print_yaml()


# START serialization_into_json()
def serialization_into_json(data):
    print(f"Serialising data to {output_file}")
    with open(output_file, mode="w") as fh:
        json.dump(data, fh, indent=" ")
# END serialization_into_json()


# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #

# START main()
def main():
    serialization_into_json(open_print_yaml())
    sys.exit(0)
# END main()


if __name__ == "__main__":
    main()
else:
    sys.exit(1)
