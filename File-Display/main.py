#
# Myles Tollefson
# Date 3/16/2025
# File Display Programming Project
# COSC 1010
#

# Defines the main function
def main ():

    # Opens the numbers file.
    numbers = open("/workspaces/COSC1010/File-Display/numbers.txt","r")

    # Defines the line variable to be used in the while
    # loop to check to see if it hit the end of the file
    # and reads the first line of the file.
    line = numbers.readline()

    # Checks to see if the loop has reached the end of the document.
    while line != '':

        # Prints the numbers in the file and stips the /n from the number.
        print (line.rstrip())

        # Primes for the next loop and reads the next line of the file.
        line = numbers.readline()

    # Closes the file. 
    numbers.close

# Runs the main function.
if __name__ == '__main__':
    main()