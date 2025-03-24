#
# Myles Tollefson
# 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Defines the main function.
def main ():
    
    # this is the acumilator for the readline loop 
    amount = 0

    # This opens the numbers file.
    numbers = open('numbers.txt','r')

    # Stores numbers retrieved in there respective variables.
    
    amount = amount + int(numbers.readline())
    
    while numbers != '':

        amount = amount + int(numbers.readline())

    # Closes the numbers file.
    numbers.close
    
    # Calculates the average.
    average = amount/3

    # Prints the resulting average.
    print(average)

# Calls the main function.
if __name__ == '__main__':
    main()