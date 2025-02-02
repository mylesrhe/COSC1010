#
# myles tollefson
# 2/2/2025
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
state_tax_puchase = 0
county_tax_puchase = 0
total_tax = 0
total = 0
# Constants for the state and county tax rates
state_tax, county_tax = 0.05, 0.025
# Get the amount of the purchase.
purchase = float(input("please input amount of purchase "))
# Calculate the state sales tax.
state_tax_puchase = state_tax * purchase
# Calculate the county sales tax.
county_tax_puchase = county_tax * purchase
# Calculate the total tax.
total_tax = county_tax_puchase + state_tax_puchase
# Calculate the total of the sale.
total = total_tax + purchase
# Print information about the sale.
print (f'amount is ${purchase:,.2f}')
print (f'total state tax is ${state_tax_puchase:,.2f}')
print (f'total county tax is ${county_tax_puchase:,.2f}')
print (f'total tax is ${total_tax:,.2f}')
print (f'your total is ${total:,.2f}')