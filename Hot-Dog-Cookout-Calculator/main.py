#
# Myles Tollefson
# 2/7/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# constants 
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# local variables 
people_attending = 0         # num people attending
num_hotdogs_per_person = 0   # num of hotdogs and buns per person
total = 0                    # total num of hotdogs and buns
min_dogs = 0                 # min number of packages of hot dogs 
min_buns = 0                 # min number of packages of buns 
dogs_left = 0                # hot dogs left over in a package   
buns_left = 0                # hot dog buns left over in a package

# get how many people are attending from user
people_attending = int(input('enter how many people are attending '))

# get how many hot dogs per person from user
num_hotdogs_per_person = int(input('enter the number of hot dogs per person '))

# calculate total number of hot dogs and buns needed 
total = num_hotdogs_per_person * people_attending

# calculate minimum number of hotdog packages needed 
min_dogs = total // HOT_DOGS_PER_PACKAGE

# determine if num of people attending is large enough to need more than one package of hot dogs
if min_dogs > 0:
    
    # calculate the number of hot dogs left over from a package (if any)
    dogs_left = total % HOT_DOGS_PER_PACKAGE

    # if there will be leftovers add an additional package of hot dogs
    if dogs_left !=0: 
        min_dogs = min_dogs + 1

#set the min num of hotdogs to one because the number of people attending is
#small enough to only need one package
else: 
    min_dogs = 1 
    
# determine left over hot dogs (if any)
dogs_left = (HOT_DOGS_PER_PACKAGE * min_dogs) - total

# calculate minimum number of hotdog bun packages needed 
min_buns = total // BUNS_PER_PACKAGE

# determine if num of people attending is large 
# enough to need more than one package of hot dog buns
if min_buns> 0:
    
    # calculate the number of hot dog buns left over from a package (if any)
    buns_left = total % BUNS_PER_PACKAGE

    # if there will be leftovers add an additional package of hot dog buns
    if buns_left !=0: 
        min_buns = min_buns + 1

#set the min num of hotdog buns to one because the number of people attending is
#small enough to only need one package
else: 
    min_buns = 1 
    
# determine left over hot dog buns (if any)
    buns_left = (BUNS_PER_PACKAGE * min_buns) - total

# display the minimum packages of hot dogs needed 
print ("minimum packages of hot dogs is",min_dogs)

# display the minimum packages of hot dog buns needed 
print ("minimum packages of hot dog buns needed is",min_buns)

# display the amount of leftover hot dogs
print ("the amount of left over hot dogs will be",dogs_left)

# display the amount of left over hot dog buns
print ("the amount of left over hot dog buns will be",buns_left)