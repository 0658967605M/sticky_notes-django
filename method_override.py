# Take user inputs that ask for the name, age, hair colour,
# and eye colour of a person'''
name = input("Enter your name: ")
age = input("Enter your age: ")
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")

# Create an Adult class with the above attributes
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = int(age)
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

# '''A method called can_drive() which prints the name of the person and 
# that they are old enough to drive.'''

    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} is old enough to drive.")
        else:
            print(f"{self.name} is not old enough to drive.")

# Create a subclass of the Adult class named Child that has the same attributes

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")
        
#  Create some logic that determines if the person is 18 or older and can drive 

if int(age) >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

person.can_drive()
