#Users age and store in a variable called age
age = input("What is your age? ")
age = int(age)

#Use the if, elif, else statements to determine the user's age group
if age > 100:
    print("Sorry, you're dead")
elif age >= 60:
    print("Enjoy your retirement")
elif age >= 40:
  print("You're over the hill")
elif age == 21:
  print("Congrats on your 21st")
elif age < 13:
  print("You qualify for kiddie discount")
else:
    print("Age is but a number")  