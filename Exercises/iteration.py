#!/usr/bin/python3

"""
Create a range from 1 to 100 and with a for loop print the square of the current number.

Add logic to test if the value of the square has reached 6,400 and if so break from the loop.

Print a message to say why the program has broken from the loop at this point.
"""
for i in range(100):
    if i**2 > 6400:
        print("The loop can not reach over 6400.")
        print("\n")
        break
    print(i**2)

"""
Create a range from 10 to 100 in steps of 5 and assign it to a variable. Print the type and content of the variable.
"""

number_range = range(10, 101, 5)
print(type(number_range))
print(number_range)
print("\n")

"""
Loop through the range variable and print the position of the current iteration as the value of the iteration with a
double dash between them ( -- ). Hint: enumerate.
"""
for position, number in enumerate(number_range):
    print(f"Position {position + 1} -- {number}")
print("\n")

"""
Convert the range in instruction 5 to a list.

Use a while loop to print the first six values of the list in instruction 7.
"""
list_nr = list(number_range)
count = 0
while count < 6:
    print(number_range[count])
    count += 1

