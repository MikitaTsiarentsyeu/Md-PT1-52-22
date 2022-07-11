# Without entering data and importing math:
# ---------------------------
import math
print('\n')
sum = 20000
t = 5
per = 15

D = sum * ((1 + (per/100)/12)**(t*12))
print('Calculated value is: %.2f BYN\n' % D)

# With entering data and importing math:
# --------------------------

sum = input('Enter the sum of the deposit: \n')
t = input('Enter the deposit term: \n')
per = input('Enter the percent: \n')
val = input('Would you like to capitalize your deposit monthly? (y/n): \n')

sum = int(sum)
t = int(t)
per = int(per)

if (val == 'y'):
    D = sum * math.pow((1 + (per/100)/12), (t*12))
    print('Calculated value of the deposit is: %.2f BYN' % D)
    print('\n')
elif (val == 'n'):
    D = sum * (1 + (per/100*t))
    print('Calculated value of the deposit is: %.2f BYN' % D)
    print('\n')
else:
    print('Incorrectly! Reload the program.')