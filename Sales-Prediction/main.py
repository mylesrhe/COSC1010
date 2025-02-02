#
# myles tollefson
# 2/2/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
PROFFIT = 0.23
# Get the amount of projected sales.
total_sales = float(input('please input total projected sales '))
# Calculate the projected profit.
total_proffit = total_sales * PROFFIT
# Print the projected profit.
print (f"proffit is projected to be ${total_proffit:,.2f}")