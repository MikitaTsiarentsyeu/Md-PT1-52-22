from decimal import *

initial_amount = float(input('Please, enter the initial deposit amount: \n'))
term_in_years = int(input('Please, enter the term of the deposit in years: \n'))
interest_rate = float(input('Please, enter the interest rate: \n'))

term_in_days = term_in_years * 365  

deposit_income = Decimal(initial_amount*(1+interest_rate/(365*100))**term_in_days)

print (f'The deposit income will be: {deposit_income.quantize(Decimal("1.00"), ROUND_HALF_UP)} ')

