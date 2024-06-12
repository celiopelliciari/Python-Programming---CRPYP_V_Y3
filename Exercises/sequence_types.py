#!/usr/bin/python3

"""
Sequence Types in Python3
"""

# Declare a dictionary called dict_.
dict_ = {}

# Create a list called list_ of all the letters in the English alphabet.
list_ = [chr(i) for i in range(97, 123)]  # lowercase letters

"""
Loop through the list list_ and count, create a dictionary dict_ with the letter
 as the key and the loop number + 1 as the value. i.e. a:1 b:2 c:3 etc...
"""
for index, char in enumerate(list_, start=1):
    dict_[char] = index

# Confirm the dict_ type and contents.
print(type(dict_))
print(dict_)
print('\n')

# Create a tuple, tuple_ from the list, list_ and confirm its type and contents.
tuple_ = tuple(list_)
print(type(tuple_))
print(tuple_)
print('\n')

# Extend the list, list_ with the list ‘A’, 'B', 'C' and confirm its type and contents.
list_.extend([chr(i) for i in range(65, 91)])  # uppercase letters

# Lowercase all elements in the list.
list_ = [letter.lower() for letter in list_]

# Create a new list, list2_ from the keys in the dictionary
list2_ = [key for key in dict_]

# Test if list2_ is a subset of list_.
list2_is_subset = all(item in list_ for item in list2_)
print("list2_ is a subset of list_: ", list2_is_subset)
print("\n")

# Print the keys in the dictionary with underscores (_) between them.
for key in dict_:
    print(key, end="_")
print("\n")

""" 
Create a dictionary with each classmate name as the key and the last educational 
course they are on, print the resulting type and dictionary.
"""
class_mates = {"John O'Neill": "Python Programming - CRPYP_V_Y3 PROGH3R08",
               "Leonardo Dias de Souza": "Python Programming - CRPYP_V_Y3 PROGH3R08",
               "Lisa Moore": "Python Programming - CRPYP_V_Y3 PROGH3R08",
               "Jamie Fennelly": "Python Programming - CRPYP_V_Y3 PROGH3R08",
               "Ciaran Cullen": "Python Programming - CRPYP_V_Y3 PROGH3R08"}
print(type(class_mates))
print(class_mates)
