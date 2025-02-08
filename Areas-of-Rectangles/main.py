#
# Myles Tollefson
# 2/8/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
rect_A_L = 0    # length of rectangle A
rect_A_W = 0    # width of rectangle A
rect_B_L = 0    # lenght of rectangle B
rect_B_W = 0    # width of rectangle B
rect_A_area = 0 # area of rectangle A 
rect_B_area = 0 # area of rectangle B
# Get length A
rect_A_L = int(input("please input the length of rectangle A "))
# Get width A
rect_A_W = int(input("please input the width of rectangle A "))
# Get length B
rect_B_L = int(input("please input the length of rectangle B "))
# Get width B
rect_B_W = int(input("please input the width of rectangle B "))
# Calculate area A
rect_A_area = rect_A_L * rect_A_W
# Calculate area B
rect_B_area = rect_A_L * rect_B_W
# Print area comparison using if-elif-else statements
# rectangle A is bigger than rectangle B
if rect_A_area > rect_B_area :
    print ("rectangle A's area is bigger than rectangle B's")

# rectangle B is bigger than rectangle A
elif rect_A_area < rect_B_area :
    print ("rectangle B's area is bigger than rectangle A's")

# both rectangle A and B have the same area
else :
    print ("both rectangle A and rectangle B have the same area")