import math
import decimal

print("-=======Program for calculating compound interest=======-")
number_of_yaers = int(input("Please enter the deposit period (years):\n"))
initial_0f_deposit = decimal.Decimal(input("Please enter the initial deposit (BUN):\n"))
annual_percentage = decimal.Decimal(input("Please enter the annual percentage (%):\n"))
monthly_capitalization = int(input("Enter 1 (Yes) or 0 (No) to account for monthly capitalization (1 or 0):\n"))

while True:
    if monthly_capitalization == 0:
        estimated_amount = initial_0f_deposit*pow((1+(annual_percentage/100)),number_of_yaers)
        print("Initial deposit =",initial_0f_deposit)
        print("Interest accrual =",round(estimated_amount-initial_0f_deposit))
        print("Total =",round(estimated_amount))
        break
    elif monthly_capitalization == 1:
        estimated_amount = initial_0f_deposit*pow((1+(annual_percentage/(100*12))),number_of_yaers*12)
        print("Initial deposit =",initial_0f_deposit)
        print("Interest accrual =",round(estimated_amount-initial_0f_deposit))
        print("Total =",round(estimated_amount))
        break
    else:
        print("Wrong input, enter 1 or 0")
        monthly_capitalization = int(input("Enter 1 (Yes) or 0 (No) to account for monthly capitalization (1 or 0):\n"))
        continue


    


    