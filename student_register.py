# Write a program that allows a user to register students for an exam venue.
# Ask the user how many students are registering

open_file = open("reg_form.txt", "r+")

student_count = int(input("How many students are registering? "))

for i in range(student_count):
    id_number = input("Enter ID number: ")
    open_file.write(id_number + "\n")

# Each student's ID number should be signed on the dotted line by the student.
for i in range(student_count):
    signature = input("Sign ID number (id_number): ")
    open_file.write(signature + "\n")

open_file.close()
# and then prompt them to sign each student's ID number.
# The ID numbers should be stored in a file called reg_form.txt.
