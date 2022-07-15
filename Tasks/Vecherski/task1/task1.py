import decimal, re
from tracemalloc import stop

def monthly_capitalization_calculate(p,t,r,n):
    '''
    What data does the function take
        p - deposit amount
        t - years amount
        r - annual interest rate
        n - how many times a year is the interest rate calculated
    '''
    p, t, r, n = decimal.Decimal(p), decimal.Decimal(t), decimal.Decimal(r), decimal.Decimal(n)
    summ = round((p * pow((1 + r / (100 * n)),(t * n))),2)
    print(f"In {years_amount} years you'll have {summ} {currency} in your account")
    Profit = summ - p
    print(f'Profit will be {Profit} {currency}') 

print(f'Bank "Nadurim & Co" offers you to open a deposit\nEnter the deposit amount:')
deposit_amount = input().replace(',', '.')
deposit_amount = re.sub ('[^\d.]', "", deposit_amount)

print(f'Enter deposit currency :')
currency = input()

print(f'How many years deposit?')
years_amount = input().replace(',', '.')
years_amount = float(re.sub ('[^\d.]', "", years_amount))

print(f'What annual interest rate would you like? :')
annual_interest_rate = input()
annual_interest_rate = re.sub ('[^\d.]', "", annual_interest_rate)

print(f'Monthly, quarterly or annual capitalization? \n\
For monthly enter 1, for quarterly enter 2, for yearly enter 3 (Default - monthly):')
capitalization_type = int(input())

capitalization_frequency = 12
if capitalization_type == 2:
    capitalization_frequency = 4
elif capitalization_type == 3:
    capitalization_frequency = 1
    if years_amount < 1:
        print(f'Wrong COMBO, bro ;) Annual capitalization is possible when the deposit period exceeds one year')
        exit()

monthly_capitalization_calculate(deposit_amount,years_amount,annual_interest_rate,capitalization_frequency)






    

    
