#
# Myles Tollefson
# 3/16/2025
# Exception Handling Programming Project
# COSC 1010
#
# Defines the main function.
def main ():
    try:
        # This opens the numbers file.
        numbers = open('/workspaces/COSC1010/Average-of-Numbers/numbers.txt','r')

        # Stores numbers retrieved in there respective variables.
        num1 = int(numbers.readline())
        num2 = int(numbers.readline())
        num3 = int(numbers.readline())

        # Calculates the average.
        average = (num1+num2+num3)/3

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