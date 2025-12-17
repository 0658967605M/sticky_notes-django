# Function to print dictionary values given the keys
# '''The loop variable 'k' in (print(dictionary[k]) should be
#  'key' to access the dictionary values'''
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Print dictionary values from simpson_catch_phrases
# syntax error on 'd'oh!' its supposed to be "d'oh!"
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }

# runtime error: missing closing bracket
# The list was supposed to be added in the hard brackets []
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
