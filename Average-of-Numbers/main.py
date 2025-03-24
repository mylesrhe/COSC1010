#
# Myles Tollefson
# 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Defines the main function.
def main ():
    
    # This is the accumulator for the loop. 
    amount = 0

    # This opens the numbers file.
    numbers = open('numbers.txt','r')
    
    # A for loop that runs for each line in the txt file.
    for line in numbers:
       
       # Adds the amount read from the txt file and adds it to the accumulator.
       amount = amount + int(line)
    
    # Closes the numbers file.
    numbers.close
    
    # Calculates the average.
    average = amount/3

    # Prints the resulting average.
    print(average)

# Calls the main function.
if __name__ == '__main__':
    main()