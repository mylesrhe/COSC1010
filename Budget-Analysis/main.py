#
# Myles Tollefson
# 2/16/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# done on several cups of coffee first thing in the morning LOL

# variables
# amount entered each time at the beginning of the loop
# is set to just above zero to initiate the loop
money = 0.0001 
budget = 0 # amount budgeted
final_expenses = 0 # running total
budget_leftover = 0
# enters amount budgeted for the month
budget = float(input('how much have you budgeted for the month '))

# loop if budget is less than zero, re enter
while budget <= 0:
     budget = float(input('please enter a number greater than zero '))
# loop, if amount enterd is equal to zero the loop will end
while money != 0:
    money = float(input("enter expenses for the month, if done enter '0' "))
# checks to see if number is valid   
    while money < 0:
         money = float(input("please enter a number greater than zero, if done enter '0' "))
    # adds money to final expenses
    final_expenses = final_expenses + money
# subtracts budget from final expenses
budget_leftover = budget - final_expenses
# prints amount over 
# if budget left-over is greater than 0 displays 
if budget_leftover > 0:
    print (f'you have {budget_leftover:.2f} left over')
# else displays that you are over your budget
else: print (f'you are over {budget_leftover:.2f}')
