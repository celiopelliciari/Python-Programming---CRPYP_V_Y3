#! /usr/bin/env python3

# Import modules
import sys

# Create a student class
class Student:
    '''Common base class for all students'''

    student_count = 0
    pad = 8       

    def __init__(self, name, course, points):
        self.name = name
        self.course = course
        self.points = points
        Student.student_count += 1
   
    def displayCount(self):
        return (f"Total Students: {Student.student_count}\n")

    def displayStudent(self):
        n = f"{'Name':<{self.pad}}: {self.name}"
        c = f"{'Course':<{self.pad}}: {self.course}"
        p = f"{'Points':<{self.pad}}: {self.points}"
        return (f"{n}\n{c}\n{p}\n")

# Generate some objects in the Student class
student = list()
student.append(Student('Jovia', 'Electrical Eng', 455))
student.append(Student('Calvin', 'Computer Eng', 440))
student.append(Student('Brenda', 'Telecoms Eng', 460))
student.append(Student('Conrad', 'Computer Eng', 445))

# Printing student count from outside an instance 
label = 'Number of students'
print (f"\n{label}\n{'-' * len(label)}\n")

print(f'Student count: {Student.student_count}\n')

# Loop through student list
label = 'All printed from within each instance'
print (f"\n{label}\n{'-' * len(label)}\n")

count = 0
for x in student: 

    # print student number in list
    print(f'Student[{count}]')  
    count += 1   

    # Print instance ID
    print(f'Instance ID : {id(x)}')

    # Print reference count
    print(f'Ref count   : {sys.getrefcount(x)}')

    # Print type of each instance
    print(f'Value       : {x}')
    print(f'Type        : {type(x)}\n')

    # Printing student information from within each instance
    print({x.displayStudent()})

    # Printing student count from within each instance
    print(x.displayCount())

    # Print line that is the length of x + 14 characters
    print('-' * (len(str(x)) + 14))

# Making changes to attributes of an instance
label = 'Changing attributes'
print (f"\n{label}\n{'-' * len(label)}\n")

# Modify some attributes
print('modifying : student[0].points = 600') 
print('modifying : student[1].course = Computer Science') 
print("modifying : student[2].misc = 'Sport: Rugby'\n") 

student[0].points = 610                   # Modify the 'points' attribute
student[1].course = 'Computer Science'    # Modify 'course' attribute
student[2].misc = 'Sport: Rugby'          # Add a 'misc' attribute
 
# Check which students have 'misc' values
for c, s in enumerate(student):
    try:
        print(f"student[{c}] misc value is {getattr(s, 'misc')}")
    except:
        print(f"student[{c}] 'misc' value is {hasattr(s, 'misc')}")

label = 'Relooking at student[2]'
print (f"\n{label}\n{'-' * len(label)}\n")

print(student[2].displayStudent())
print(f'Misc  :  {student[2].misc}\n')

# Delete the 'misc' for student[2]
print("Deleting the 'misc' attribute for student[2]")
delattr(student[2], 'misc')                 

# Test for the 'misc' object for student[2]
print(f"student[2] 'misc' value is {hasattr(student[2], 'misc')}\n")

label = 'Accessing built-in attributes'
print (f"\n{label}\n{'-' * len(label)}\n")

# Accessing class built-in attributes
print (f'{Student.__dict__}\n')    # Dictionary of class namespace
print (f'{Student.__doc__}\n')     # Class docstring or none, if undefined
print (f'{Student.__name__}\n')    # Class name
print (f'{Student.__module__}\n')  # Module name in which the class is defined
print (f'{Student.__bases__}\n')   # Tuple containing the base classes

# // End //

