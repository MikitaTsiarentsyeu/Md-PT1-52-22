x = input ('Please enter your name:\n')
print ('Hello,', x, end = '!\n')
answer = input('Would you like to calculate deposit (y/n)?\n')
if answer == 'y':
    p = int(input('Enter the deposit amount in BYN\n'))
    if p<=0:
        print ('Incorrect')
    r = int(input('Enter the deposit interest rate in %\n'))
    if r<=0:
        print ('Incorrect')
    t = int(input('Enter the deposit term in years\n'))
    if t<=0:
        print ('Incorrect')
    a = input('What kind of capitalization do you want to have? Please type m for "month" or y for "years"\n')
    if a == 'm': 
        c = p*((1+r/100/12)**(t*12))
        print('Your month amount is', int(c))
    elif a == 'y':
        c = p*(1+(r/100*t))
        print('Your year amount is', int(c))

elif answer == 'n':
 print('Understandable. Have a nice day,', x, end = '!')
else:
    print ('Error. Please try again!')




