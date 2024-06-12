#! /usr/bin/env python3
""" JSON processing """

import json
import pprint

# Variables //
file = "data_set.json"
new_file = "data_set2.json"

# // De-serialise data from the file (read it) //
print(f"De-serialising data from '{file}'")
with open(file, mode="r") as fh:
    data = json.load(fh)

print(f"\n{type(data)}, {data}\n")

# // Add 'rugby' as a hobby //
print("Adding 'rugby' as a new hobby")
data["hobbies"].append("rugby")

# // Add a new child //
print("Adding a new child called 'Orla'")
_ = {"firstName": "Orla", "age": 1}
data["children"].append(_)

# // Serialise data to the file (write it) //
print(f"Serialising data to '{new_file}'\n")
with open(new_file, mode="w") as fh2:
    json.dump(data, fh2, indent=("  "))
    # json.dump(data, fh2)

# // End //
exit()
