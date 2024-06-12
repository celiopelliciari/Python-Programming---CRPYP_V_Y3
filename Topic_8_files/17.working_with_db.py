#! /usr/bin/env python3

import pprint
import sqlite3
import sys

# Defined variables
database = "db_2.sqlite"
table = "class_list"
columns = {
    "ref_no": "INTEGER PRIMARY KEY",
    "fname": "TEXT",
    "sname": "TEXT",
    "number": "INTEGER",
}
data = (
    (0, "Tom", "Ryan", 111111),
    (1, "Mary", "Murphy", 222222),
    (2, "Ada", "Lovelace", 333333),
    (3, "Charles", "Babbage", 444444),
)
list_ = list()
str_ = str()
tuple_ = tuple()

# // Query Function //
def query_(query):
    """Query function for the Database"""

    list_ = list()
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        cur.execute(query)
        list_ = cur.fetchall()  # Empty except for SELECT
        cur.close()  # Close database cursor
        con.commit()  # Commit labels to the database
    return (0, list_)


# // Use SQL to drop a 'class_list' table if it currently exists //
print(f"Dropping '{table}'' from the db '{database}' if it exists")
query_(f"DROP TABLE IF EXISTS {table}")

# // Use SQL to create new 'class_list' table //
print(f"Creating '{table}'' in the '{database}' db")
for (key, value) in columns.items():
    list_.append(f"{key} {value}")
str_ = ", ".join(list_)
query_(f"CREATE TABLE IF NOT EXISTS {table} ({str_})")

# // Get input and put in the database table 'class_list' //
str_ = ", ".join(columns.keys())
for d in data:
    print(f"Inserting {d} into the '{table}' table")
    query_(f"INSERT INTO {table} ({str_}) VALUES {d}")

# // Getting data from database table 'class_list' //
print(f"Retrieving {d} from the '{table}' table")
(_, list_) = query_(f"SELECT * FROM {table}")

# // Printing table 'class_list' //
for t in list_:
    print("   ", ", ".join([str(e) for e in t]))

# // End //
sys.exit(0)
