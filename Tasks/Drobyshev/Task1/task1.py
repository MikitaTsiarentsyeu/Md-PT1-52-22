print ('Deposit: initial amount - 20000 BYN; term - 5 years; interest (annual) - 15%; !monthly capitalization! '
'Calculate the amount on the account at the end of the specified period.') 
print ('Answer: The amount = 42143.63 BYN')

print ('To check my solution, as well as to calculate the compound interest using your data, use the form below.')

while True:
    amount = input ('Please enter the amount of the initial payment, BYN: \n')
    try:
        amount = float (amount)
        break
    except :
        print ('You have entered the letters, try again.') if amount.isalpha() else print ('You have entered incomprehensible characters, try again.')

while True:
    add = input ('Please enter the amount of the monthly deposit, BYN: \n')
    try:
        add = float (add)
        add >= 0
        break
    except :
        print ('You have entered the letters, try again.') if add.isalpha() else print ('You have entered incomprehensible characters, try again.')
            
while True:
    term = input ('Please enter the deposit term, years: \n')
    try:
        term = float (term)
        result = 1 / term
        break
    except ZeroDivisionError:
        print('You have entered the number 0, try again.')
    except :
        print ('You have entered the letters, try again.') if term.isalpha() else print ('You have entered incomprehensible characters, try again.')
            
while True:
    rate = input ('Please enter the annual interest rate, % : \n')
    try:
        rate = float (rate)
        result = 1 / rate
        break
    except ZeroDivisionError:
        print('You have entered the number 0, try again.')
    except:
        print ('You have entered the letters, try again.') if rate.isalpha() else print ('You have entered incomprehensible characters, try again.') 
           
month = term * 12
total = amount * (1 + rate/100/12) ** month
sum = (add * ((1 + rate/100/12) ** (month-1))*(1 + rate/100/12) - add * (1 + rate/100/12)) / (rate/100/12)
total_sum = total + sum
profit = total_sum - add*(month-1) - amount 
profitability = (profit/(amount+add*(month-1))*100)/term

print (f'The amount = {total_sum:.2f} BYN' )
print (f'Profit = {profit:.2f} BYN')
print (f'The yield was (as a percentage per annum) = {profitability:.2f} %')