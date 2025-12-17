#Ask the user to enter three different integers
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

#print out the integers
print("The three integers are:", num1, num2, num3)

#the sum of all the numbers
total = num1 + num2 + num3
print("The sum of the three integers is:", total)

#The first number minus the second number
difference = num1 - num2
print("The difference between the first and second integers is:", difference)

#The third number multiplied by the first number
product = num3 * num1
print("The product of the third and first integers is:", product)

#The sum of three numbers divided by the first number
if num1 != 0:
    division = total / num1
    print("The sum of the three integers divided by the first integer is:", division)
else:
    print("Division by zero is not allowed.")
