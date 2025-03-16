#
# Myles Tollefson
# 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#

def main ():
# opens numbers file
    numbers = open('/workspaces/COSC1010/Average-of-Numbers/numbers.txt','r')

    # stores numbers retrieved in respective variables
    num1 = int(numbers.readline())
    num2 = int(numbers.readline())
    num3 = int(numbers.readline())

    # calculates average
    average = (num1+num2+num3)/3

    # prints average
    print(average)

#call the main function
if __name__ == '__main__':
    main()