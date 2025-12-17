# '''Write the program that reads the data and prints out the names
# and birth dates in two different sections'''

# The data will be read from the file DOB.txt
open_file = open("DOB.txt", "r+")

print("\nNames: ")
for line in open_file:
    result = line.split()
    print(result[0], result[1])

open_file = open("DOB.txt", "r+")

print("\nBirthdates: ")
for line in open_file:
    result = line.split()
    print(result[2], result[3], result[4])


open_file.close()
