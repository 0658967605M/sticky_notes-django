# '''Ask the user to enter the number continually, 
# if the user enters -1, the program should quit.'''
while True:
    number = int(input("Enter a number : "))

    if number == -1:
        print("Exiting the program.")
        break

    elif number != -1:
        print(f"You entered: {number}")
else:
    print("Invalid input, please try again.")  