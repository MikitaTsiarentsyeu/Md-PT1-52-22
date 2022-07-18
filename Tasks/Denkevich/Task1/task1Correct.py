import decimal

# Without entering data:
print('\n')
sum = decimal.Decimal('20000')
t = decimal.Decimal('5')
per = decimal.Decimal('15')

D = sum * ((1 + (per/100)/12)**(t*12))
print('Calculated value is: %.2f BYN' % D, '\n')

# With entering data:
sum = decimal.Decimal(input('Enter the sum of the deposit: \n'))
t = decimal.Decimal(input('Enter the deposit term: \n'))
per = decimal.Decimal(input('Enter the percent: \n'))
val = input('Would you like to capitalize your deposit monthly? (y/n): \n')

if (val == 'y'):
    D = (sum * ((1 + (per/100)/12)**(t*12)))
    print('Calculated value of the deposit is: %.2f BYN' % D, '\n')
elif (val == 'n'):
    D = (sum * (1 + (per/100*t)))
    print('Calculated value of the deposit is: %.2f BYN' % D, '\n')
else:
    print('Incorrectly! Reload the program.')