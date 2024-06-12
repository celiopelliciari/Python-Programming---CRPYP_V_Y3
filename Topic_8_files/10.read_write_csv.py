#! /usr/bin/env python3
""" CSV Read """

import csv

header = list()
data = list()
orders_csv = "orders.csv"
orders2_csv = "orders2.csv"
new_data = ["14/5/2021", "West", "Duggan", "Stapler", "5", "15", "75"]

# // Open CSV file as a file-handle for reading //
with open(orders_csv, mode="r", encoding="utf8") as fh:
    data = list(csv.reader(fh))

# // Append 'new_data' to 'data' list
data.append(new_data)

# // Open CSV file as a file-handle for writing //
with open(orders2_csv, mode="w", encoding="utf8") as fh:
    writer = csv.writer(fh)
    writer.writerows(data)

# // End //
