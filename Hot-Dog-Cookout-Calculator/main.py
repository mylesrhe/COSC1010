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
people_atending = 0          # num people atending
num_hotdogs_per_person = 0   # num of hotdogs and buns per person
total = 0                    # total num of hotdogs and buns
min_dogs = 0                 # min number of packages of hot dogs 
min_buns = 0                 # min number of packages of buns 
dogs_left = 0                # hot dogs left over in a package   
buns_left = 0                # hot dog buns left over in a package

# get how many people are atending from user
people_atending = int(input('enter how many people are atending '))

# get how many hot dogs per person from user
num_hotdogs_per_person = int(input('enter the number of hot dogs per person '))

# calculate total number of hot dogs and buns needed 
total = num_hotdogs_per_person * people_atending

# calculate minimum number of hotdog packages needed 
min_dogs = total // HOT_DOGS_PER_PACKAGE

# determine if num of people atending is large enough to need more than one package of hot dogs
if min_dogs > 0 :
    # calculate the number of hot dogs left over from a package (if any)
    dogs_left = total % HOT_DOGS_PER_PACKAGE
# determine left over hot dogs (if any)

