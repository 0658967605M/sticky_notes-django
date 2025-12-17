#Ask the user for a sentence and store users response in a variable
sentence = input("Please enter a sentence: ")
print(sentence)
str_manip = sentence

#Calculating and displaying the length of the sentence
length = len(str_manip)
print("Length of the sentence:", length)

#Find the last letter in str_manip and replace it with the occurrence @
if length > 0:
    last_char = str_manip[-1]
    str_manip = str_manip[:-1] + '@'
    print(str_manip)

    #Find the last 3 characters in str_manip backwards
    last_three_chars = str_manip[-3:][::-1]
    print("Last 3 characters (backwards):", last_three_chars)

    #Create five-letter word that is made up of the last three characters and the first two characters in str_manip
    five_letter_word = last_three_chars + str_manip[:2]
    print("Five-letter word:", five_letter_word)
