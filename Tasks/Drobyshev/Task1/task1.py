import decimal

print ('Deposit: initial amount - 20000 BYN; term - 5 years; interest (annual) - 15%; !monthly capitalization! '
'Calculate the amount on the account at the end of the specified period.') 
print ('Answer: The amount = 42143.63 BYN')

print ('To check my solution, as well as to calculate the compound interest using your data, use the form below.')

while True:
    amount = input ('Please enter the amount of the initial payment, BYN: \n')
    try:
        amount = decimal.Decimal (amount)
        assert amount >= 0
        break
    except AssertionError: 
        print ('You entered a negative number, please try again.')
    except :
        print ('You have entered the letters, please try again.') if amount.isalpha() else print ('You have entered incomprehensible characters, please try again.')

while True:
    add = input ('Please enter the amount of the monthly deposit, BYN: \n')
    try:
        add = decimal.Decimal (add)
        assert add >= 0
        break
    except AssertionError: 
        print ('You entered a negative number, please try again.')
    except :
        print ('You have entered the letters, try again.') if add.isalpha() else print ('You have entered incomprehensible characters, please try again.')
            
while True:
    term = input ('Please enter the deposit term, years: \n')
    try:
        term = decimal.Decimal (term)
        result = 1 / term
        assert term > 0
        break
    except AssertionError: 
        print ('You entered a negative number, please try again.')
    except ZeroDivisionError:
        print('You have entered the deposit term = 0, please try again.')
    except :
        print ('You have entered the letters, please try again.') if term.isalpha() else print ('You have entered incomprehensible characters, please try again.')
            
while True:
    rate = input ('Please enter the annual interest rate, % : \n')
    try:
        rate = decimal.Decimal (rate)
        result = 1 / rate
        assert rate > 0
        break
    except AssertionError: 
        print ('You entered a negative number, please try again.')
    except ZeroDivisionError:
        print('You have entered the annual interest rate = 0, please try again.')
    except:
        print ('You have entered the letters, please try again.') if rate.isalpha() else print ('You have entered incomprehensible characters, please try again.') 

month = term * 12
total = amount * (1 + rate/100/12) ** month
sum = (add * ((1 + rate/100/12) ** (month-1))*(1 + rate/100/12) - add * (1 + rate/100/12)) / (rate/100/12)
total_sum = total + sum
profit = total_sum - add*(month-1) - amount 
profitability = (profit/(amount+add*(month-1))*100)/term

print (f'The amount = {total_sum:.2f} BYN' )
print (f'Profit = {profit:.2f} BYN')
print (f'The yield was (as a percentage per annum) = {profitability:.2f} %')