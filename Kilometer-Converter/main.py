#
# Myles tollefson
# 2/23/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Universal constant for kilometers to miles
MILES_MULTIPLYER = 0.6214

# Defines main.
def main ():
    
    # Asks for kilometer input.
    kilometer = int(input("enter kilometer amount "))
    
    # Runs kilo to mile and prints result.
    print (f"{kilometer} kilometers is {kilo_to_mile(kilometer):.2f} miles")


# Definition for kilo to mile function.
def kilo_to_mile (kilo):
    
    # Multiplies kilo to miles multiplier.
    kilo = kilo * MILES_MULTIPLYER
    
    # Returns kilo which is the final mile result.
    return kilo

# Runs main.
main()