#
# Myles Tollefson
# 4/13/2025
# Pig Latin Programming Project
# COSC 1010
#

# Defines main function. 
def main():
    # Stores an empty string that will be appended later. 
    new_string = ('')

    # Gets user input.
    phrase = input('enter a sentence to be converted ')

    # Splits the string into a list.
    phrase_list = phrase.split()

    # For loop that will iterate for every word in the list.
    for word in phrase_list:
    
        # Stores the first letter from the word in the 'first' variable.
        first = word[0:1]
    
        # If the word is two letters or longer
        # the following letters are stored in the 'second' variable. 
        if len(word) > 1:
            second = word[1:]
        
            # If the word is two letters or longer, the 'second' variable is added to the 'first' 
            # putting the first letter from the word behind all the other letters in the word and an 'ay' is added.
            new_string += str(second + first + "ay ")
    
        # If the word is only one letter an 'ay' is added.
        else:
            new_string += str(first + "ay ")

    # Prints the new string.    
    print(new_string)


if __name__ == '__main__':
    main()