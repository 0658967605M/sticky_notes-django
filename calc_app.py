import os
import math

# '''If a user chooses to perform a calculation,
#  the app should accept two numbers and an 
# operation ( +, -, *, or /) as inputs from the user'''


def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

equation = input(
    "Enter first number, second number, and\
    operation (+, -, *, /) separated by spaces: "
    )
print(f"equation: {num1} {operation} {num2}= {result}")

#'''The calculator application should allow users to 
# perform a calculation or print previous 
# calculations stored in a file called equations.txt'''


def save_equation(equation, result):
    with open('equations.txt', 'a') as file:
        file.write(f"{equation} = {result}\n")


# '''If a user chooses to print previous equations from
#  equations.txt, display all previous equations.'''


def print_previous_equations():
    if os.path.exists('equations.txt'):
        with open('equations.txt', 'r') as file:
            return file.read()
    return "No previous equations found."