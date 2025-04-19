#
# Myles Tollefson
# 4/19/2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables
    num_correct = 0 # This variable counts correct responses.
    num_incorrect = 0 # This variable counts incorrect responses.
    
    # Asks user for an amount of rounds that the quiz will last.
    num_rounds = int(input("how many rounds would you like to go? "))

    # For loop that will quiz the user.
    for count in range(num_rounds):
        
        # Grabs a random state and capital.
        state, capital = capitals.popitem()

        # Asks the question to the user.
        print("what is the capital of", state , "?", end=' ')
        response = input()

        # Checks if the answer is correct.
        if response.lower() == capital.lower():
            # Prints correct.
            print('correct')
            # Adds one to the num_correct variable.
            num_correct +=1
        
        else:
            #prints incorrect and gives the correct answer. 
            print("incorrect. the answer was", capital)
            # Adds one to the num_incorrect variable.
            num_incorrect +=1
    # Gives final score
    print("thanks for playing your score is")
    print(num_correct, 'correct')
    print(num_incorrect, 'incorrect')
    
# Call the main function.
if __name__ == '__main__':
    main()
