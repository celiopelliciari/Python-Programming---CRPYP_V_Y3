#! /usr/bin/env python3

old_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_a_list = list()

lambda_fun = lambda x: x * x

for x in old_tuple:
    new_a_list.append(lambda_fun(x))

print("A.", new_a_list)
print()

# // Using map() //
print("B.")

new_b_map = map(lambda_fun, old_tuple)
print(type(new_b_map), new_b_map)

new_b_list = list(map(lambda_fun, old_tuple))
print(type(new_b_list), new_b_list)

new_b_list = list(map(lambda x: x * x, old_tuple))
print(new_b_list)