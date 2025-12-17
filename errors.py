# This example program is meant to demonstrate errors
# '''There are some errors in this program. Run the program,
# look at the error messages, and find and fix the errors'''
# syntax error, the variable was supposed to be stored first
program_type = 'Welcome to the error program'
print("\n")

# '''Variables declaring the user's age,
# casting the str to an int, and printing the result'''
# The local error , whitespace was created before writting the program
age_str = "24"
age = (age_str)
print("I'm " + (age) + " years old.")

# Variables declaring additional years and printing the total years of age
# The local error , whitespace was created before writting the program
# The syntax error , years from now was supposed to be a string
years_from_now = "3"
total_years = int(age) + int(years_from_now)
print("In 3 years, I'll be " + str(total_years) + " years old.")

# '''The syntax error , the was no brackets from the print statement
# and the total_years was not identified as a string'''
print("The total number of years:" + str(total_years))

# '''Variable to calculate the total number of months
# from the given number of years and printing the result'''
# '''The syntax error , total was not defined it was supposed to be total_years
# and the other syntax error was the brackets from the print statement'''
# '''Runtime error , The 6 months was not added to total_months,thats why
#  the addition was not meeting requirements'''
total_months = total_years * 12
total_months += 6
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

# HINT, 330 months is the correct answer
