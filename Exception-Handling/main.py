#
# Myles Tollefson
# 3/16/2025
# Exception Handling Programming Project
# COSC 1010
#
# Defines the main function.
def main ():
    try:
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
     
    # Exception handler that is triggered when the
    # file is not found at the expected location.
    except IOError:
        print("ERROR file not found")
   
    # Exception handler that is triggered when data
    # input is not valid numbers 
    except ValueError:
        print("ERROR data type must be valid numbers")
   
    # Exception handler for unaccounted for errors
    except:
        print("ERROR an error occurred")

# Calls the main function.
if __name__ == '__main__':
    main()