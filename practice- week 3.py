# DSC 510
# Week 3 Programming assignment
# Rosie Navarro-Martinez
# 03/31/26
# Purpose: using what if statements for fiber optics cable- amount changes discounted rate.

print("welcome user! The following is more information for Fiber Optics. Depending on amount there is a discount at checkout")
company = input('enter company name:')
number_of_feet = float(input('enter number of feet:'))

#the following is the if statements: there are four different scenario therefore elif
# made "discount" in descending order
if number_of_feet > 500:
    cost_per_foot = .55
elif number_of_feet > 250:
    cost_per_foot = .75
elif number_of_feet > 100:
    cost_per_foot = .85
else:
    cost_per_foot = .95
total_cost = cost_per_foot * number_of_feet

#the following is a receipt for the customer- shows information on company name, cost, and total
print("Receipt:")
print("Company Name:", company)
print(f"Cost per foot: ${cost_per_foot: .2f}")
print(f"Total Cost: ${total_cost: .2f}")