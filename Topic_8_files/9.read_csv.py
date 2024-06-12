#! /usr/bin/env python3
""" CSV Read """

import csv

header = list()
data = list()
orders_csv = "orders.csv"

# // Open CSV file as a file-handle //
with open(orders_csv, mode="r", encoding="utf8") as fh:
    csv_read = list(csv.reader(fh))
    header = csv_read[0]
    data = csv_read[1:]

print(header)
print()
[print(x) for x in data]


# // End //
