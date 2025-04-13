#
# Myles Tollefson
# 4/13/2025
# Vowels and Consonants Programming Project
# COSC 1010
#

#defines main function
def main():
    
    # user inputs a string.
    sentence = input('enter a sentence ')

    # Runs the vowel and consonants functions 
    # from inside the print function and prints 
    # out the results showing how many vowels and 
    # consonants were in the input string.
    print("there were", vowel(sentence),'vowels and', consonants(sentence),'consonants in that sentence')

#Defines the vowel function that will check for vowels.
def vowel (sent):
    
    # This is a list of vowels that will be compared to the input string.
    vowels = ['a','e','i','o','u']

    # Running total for the number of vowels in the string.
    total_vowels = 0

    # A for loop that will compare the input string 
    # with the vowels list and add 1 to the running 
    # total for every vowel counted.
    for ch in sent: 
        if ch.lower() in vowels:
            total_vowels += 1

    # returns the running total.
    return total_vowels

# Defines consonants function that will check for consonants.
def consonants(sent):
    
    # This is a list of vowels that will be compared to the input string.
    vowels = ['a','e','i','o','u']

    # Running total for the number of consonants in the string.
    total_consonants = 0

    # A for loop that will compare the input string 
    # with the vowels list and add 1 to the running 
    # total for every vowel not counted.
    for ch in sent: 
        if ch.isalpha() and ch.lower() not in vowels:
            total_consonants += 1
    
    # Returns running total.
    return total_consonants

# runs main function
if __name__ == '__main__':
    main()





