#
# Myles Tollefson
# 4/5/2025
# Magic 8 Ball Programming Project
# COSC 1010
#

# Defines main.
def main(): 

    # Imports random module for the magic 8 ball.
    import random
    
    # Con short for continue. Variable for the while loop where the 8 ball runs.
    con = 'Y'

    # Defines empty list as magic. Will be filled up with the 8 ball responses. 
    magic = []
    
     # Opens file as ball_list.
    ball_list = open('8_ball_responses.txt','r')

    # Primes for the read line loop where the file will be processed.
    line = ball_list.readline()
    
    # Reads file and puts the contents into a list.
    while line != '':
        
        #strips the read line from its newline character
        line = line.rstrip('\n')

        # Adds the read line to the list with each loop.
        magic += [line]
        
        # Reads next line in the file.
        line = ball_list.readline()
    
    # Closes 8 ball responses file.
    ball_list.close
    
    # While loop, As long as con = Y or y it will run.
    while con == 'Y' or con == 'y':
       
        # User is prompted to input a question
        input("ask a question ")

        # A response is randomly chosen from the
        # magic list and printed in the terminal.
        print(random.choice(magic))

        # Asks user to go again, response input will be assigned to con.  
        con = input("want to go again? Y or N ")
# Runs main.
if __name__ == '__main__':
    main()