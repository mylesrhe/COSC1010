#
# Myles Tollefson
# 2/16/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
bugs = 0       # bugs collected
total_bugs = 0 # bug total
# Get number of bugs collected each day using a for loop.
for days in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    bugs = int(input(f"input number of bugs caught for {days} "))
    # checks to make sure number is not negative    
    while bugs < 0:
        bugs = int(input(f"input a number greater than zero "))
    # adds bugs entered to bug total
    total_bugs = total_bugs + bugs
# Display the total number of bugs collected.
print (f"you have caught {total_bugs} total bugs over the week")
