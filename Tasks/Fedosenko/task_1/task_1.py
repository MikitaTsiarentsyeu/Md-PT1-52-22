from decimal import *

initial_amount =  20000
term_in_years = 5
interest_rate = Decimal('0.15')

term_in_days = term_in_years * 365  

deposit_income = (initial_amount*(1+interest_rate/365)**term_in_days)

print (deposit_income)

