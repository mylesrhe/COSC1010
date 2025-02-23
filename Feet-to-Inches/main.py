#
# Myles Tollefson
# 2/23/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

INCHES_PER_FOOT = 12 # Universal constant for inches per foot.
 
feet = 0             # Feet variable.

# Defines the main function.
def main ():
    # Asks for input from user requesting amount of feet. 
    feet = int(input ("input amount of feet "))

    # Runs the feet to inches function and prints out the result.
    print (f"{feet} feet is {feet_to_inches(feet)} inches")

# Defines the feet to inches function.
def feet_to_inches (feet):
    return feet * INCHES_PER_FOOT


# Runs the main function.
main ()