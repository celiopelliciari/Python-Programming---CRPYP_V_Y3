#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================ #
# //             Module imports             // #
# ============================================ #

import sys
import csv

# ============================================ #
# //      Global variable declarations      // #
# ============================================ #

orders_csv = "orders.csv"
orders2_csv = "orders2.csv"
new_data = ["14/5/2021", "West", "Duggan", "Stapler", "5", "15", "75"]

# ============================================ #
# //                Functions               // #
# ============================================ #


# START adding_new_data()
def adding_new_data():
    with open(orders_csv, mode="r", encoding="utf8") as fh:
        data = list(csv.reader(fh))  # Read data from existing CSV

    with open(orders2_csv, mode="w", encoding="utf8") as fh:
        writer = csv.writer(fh)  # Create writer using file handle
        writer.writerows(data + [new_data])  # Write existing data plus new_data in condensed way
# END adding_new_data()


# -------------------------------------------- #
# //               main function            // #
# -------------------------------------------- #

# START main()
def main():
    adding_new_data()
    sys.exit()
# END main()


if __name__ == "__main__":
    main()
else:
    sys.exit(1)
