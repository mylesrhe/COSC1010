#
# Myles Tollefson
# 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Defines the main function.
def main ():
    # This opens the numbers file.
    numbers = open('/workspaces/COSC1010/Average-of-Numbers/numbers.txt','r')

    # Stores numbers retrieved in there respective variables.
    num1 = int(numbers.readline())
    num2 = int(numbers.readline())
    num3 = int(numbers.readline())

    # Closes the numbers file.
    numbers.close
    
    # Calculates the average.
    average = (num1+num2+num3)/3

    # Prints the resulting average.
    print(average)

# Calls the main function.
if __name__ == '__main__':
    main()