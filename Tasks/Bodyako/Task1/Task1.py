a = int(input('1. Enter the amount of deposit (USD): '))
b = int(input('2. Enter deposit interest rate (%): '))
c = int(input('3. Enter the deposit term (yers): '))
d = str(input('4. Choose the type of capitalization, type "month" or "year": '))

if d == 'month': 
    x = a*((1+b/100/12)**(c*12))
    print('Amount in the bank account at the end of the term:', round (x,2), 'USD')
elif d == 'year':
    x = a*(1+(b/100*c)) 
    print('Amount in the bank account at the end of the term:', round (x,2), 'USD')
else:
    print('Incorrect, please try again, in item 4. type "month" or "year"') 