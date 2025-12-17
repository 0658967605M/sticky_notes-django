# Store your friends names in a list variable and print the list
friends_names = ["friend_one", "friend_two", "friend_three"]
print(friends_names)

# '''Write the statement to print out the name of the first friend,
# then the name of the last friend and finally get the length of the list'''
print(friends_names[0])
print(friends_names[2])
print(len(friends_names))

# The list that stores the age of each of your friends
#'''The first entry of the list is the age of the first friend 
# named first in the other list'''
friend_one = input("Enter the age of friend one: ")
print(friend_one)
friend_two = input("Enter the age of friend two: ")
print(friend_two)
friend_three = input("Enter the age of friend three: ")
print(friend_three)
friends_ages = [friend_one, friend_two, friend_three]

# Print the name and friends age in a sentence
print(f"{friends_names[0]} is {friends_ages[0]} years old.")
print(f"{friends_names[1]} is {friends_ages[1]} years old.")
print(f"{friends_names[2]} is {friends_ages[2]} years old.")
