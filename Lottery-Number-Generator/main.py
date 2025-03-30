#
# Myles Tollefson
# 3/30/2025
# Lottery Number Generator Programming Project
# COSC 1010
#

# this imports random module.
import random

MAX_NUMBER = 7      # Defines max number of digits in lottery number.
START_NUMBER = 0    # Defines starting range in the random function.
END_NUMBER = 9      # Defines ending range in the random function.

# This defines main function.
def main():

    # Creates the empty list for the lottery numbers.
    num = [0] * MAX_NUMBER

    # This for loop fills the empty list 
    # with random numbers ranging from 0 to 9.
    for index in range (MAX_NUMBER):
        num[index] = random.randint(START_NUMBER, END_NUMBER)
    
    # Prints the lottery numbers.
    print('Your numbers are')
    for index in range (MAX_NUMBER):
        print (num[index], end = ' ')

# Runs the main function.
if __name__ == '__main__':    
    main()
