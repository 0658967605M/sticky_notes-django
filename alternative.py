# '''Ask the user to enter a string and make each
# alternate character touppercase character and each alternate
# to character to lowercase character.'''
def alternate_case(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result


user_input = input("Enter a string: ")
print(alternate_case(user_input))

# '''Start the same string but making each alternative
# world uppercase and lowercase using the
# split and join methods.'''


def alternate_case_split_join(s):
    words = s.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].upper()
        else:
            words[i] = words[i].lower()
    return ' '.join(words)


user_input = input("Enter a string: ")
print(alternate_case_split_join(user_input))
