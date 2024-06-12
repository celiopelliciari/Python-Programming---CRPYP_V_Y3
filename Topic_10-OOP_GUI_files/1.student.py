#! /usr/bin/env python3

class Student():

    def __init__(self, *args):
        print(f"Current instance ID 'Self' {id(self)}")
        self.name = args[0]
        self.name2 = args[1]

    def first(self):
        print(f"{self.name} is first name.")

    def second(self, college='South East'):
        print(f"{self.name2} is family name.")
        print(f"from the {college} Technological University Ireland.")

# Engineering object, default tribe
engineering = Student('Jovia', 'Murphy')
print('Engineering instance')
print(f"New 'engineering' instance ID: {id(engineering)}")
engineering.first()
engineering.second()

print('')

# Computing object, specified tribe
computing = Student('Brenda', 'Ryan')
print('Computing instance')
print(f"New 'computing' instance ID: {id(computing)}")
computing.first()
computing.second('Dublin')

# // End //


