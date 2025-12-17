#Save the sentence
sentence= "The!Quick!Brown!Fox!Jumps!Over!The!Lazy!Dog."
print(sentence)

#Use the replace() function to replace '!' with blank space
sentence = sentence.replace('!', ' ')
sentence = sentence.replace("The", "").replace("Quick", "").replace("Brown", "").replace("Fox", "").replace("Jumps", "").replace("Over", "").replace("The", "").replace("Lazy", "").replace("Dog", "")
print(sentence)

#Reprint the sentence using upper function
sentence = "The!Quick!Brown!Fox!Jumps!Over!The!Lazy!Dog."
sentence = sentence.upper()
print(sentence)

#Write the sentence in reverse using slicing
sentence = "The!Quick!Brown!Fox!Jumps!Over!The!Lazy!Dog."
sentence = sentence[::-1]
print(sentence)
