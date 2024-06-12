#! /usr/bin/env python3
""" Yaml processing """

import sys
import yaml
from pprint import pprint

# Variables
file = "network.yaml"
new_file = "network2.yaml"

# // Open a yaml file for reading //
with open(file, mode="r") as fh:
    head_ = fh.readline()
    net_list = yaml.load(fh, Loader=yaml.FullLoader)

print(head_)
print(type(net_list), net_list)
print()
pprint(net_list)
print()

# // Print the 'ens160' interface //
print(f"ens160: {net_list['network']['ethernets']['ens160']}\n")

# Add static address on 'ens160'
#   Address: '10.10.10.100/16
#   Nameserver:'8.8.8.8'

new_addr = {"addresses": ["10.10.10.100/16"], 
            "nameservers": {"addresses": ["8.8.8.8"]}}

# // Update the 'net_list' dictionary //
net_list["network"]["ethernets"]["ens160"] = new_addr

print(f"ens160: {net_list['network']['ethernets']['ens160']}\n")

# // Write a new network yaml file //
head2_ = "# New network2.yaml file"
print(f"{head2_}\n")
with open(new_file, "w") as fh:
    fh.write(f"{head2_}\n")
    fh.write("\n")
    yaml.dump(net_list, fh, default_flow_style=False)

# // End //
sys.exit(0)
