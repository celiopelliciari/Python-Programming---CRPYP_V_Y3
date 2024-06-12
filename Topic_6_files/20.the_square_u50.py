#! /usr/bin/env python3

old_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_list = list()
under_50_list = list()

new_list = list(map(lambda x: x * x, old_tuple))
under_50_list = list(filter(lambda x: x < 50, new_list))

print(under_50_list)
