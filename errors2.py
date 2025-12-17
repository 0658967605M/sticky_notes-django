# This example program is meant to demonstrate errors.

# '''There are some errors in this program. Run the program,
# look at the error messages, and find and fix the errors.'''
# syntax error: Lion is a string so it should be enclosed in quotes
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# syntax error: f-string is not properly formatted
# runtime error : is flake8 long statements for full_spec
full_spec = f"This is a {animal}. It is \
a {animal_type} and it has {number_of_teeth} teeth"

# syntax error: print statement should have brackets
print(full_spec)
