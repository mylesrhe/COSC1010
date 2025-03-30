#
# myles tollefson
# 3/30/2025
# Lottery Number Generator Programming Project
# COSC 1010
#

# this imports random modual
import random

MAX_NUMBER = 7      # Defines max number of didgits in lotery number.
START_NUMBER = 0    # Difines starting range in the random function.
END_NUMBER = 9      # Defines ending range in the random function.

# This defines main function.
def main():

    # Creates the empty list for the lotery numbers.
    num = [] * MAX_NUMBER

    # This for loop fills the empty list 
    # with random numbers ranging from 0 to 9.
    for index in range (MAX_NUMBER):
        num[index] = random.randint(START_NUMBER, END_NUMBER)
    
    # Prints the lotery numbers.
    print('Your numbers are')
    for index in range (MAX_NUMBER):
        print (index)
