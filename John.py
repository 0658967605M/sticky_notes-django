# '''Write the program that takes in the users input as a string
# and while the string is not John, add every string until
# the user enters John , store all incorrect strings in a list'''

def main():
    user_input = ""
    incorrect_inputs = []
    while user_input != "John":
        user_input = input("Enter your name: ")
        if user_input != "John":
            print("You entered:", user_input)
            incorrect_inputs.append(user_input)
    print("Incorrect input names:", incorrect_inputs)


if __name__ == "__main__":
    main()
