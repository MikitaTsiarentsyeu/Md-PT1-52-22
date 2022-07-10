print ('Deposit: initial amount - 20000 BYR; term - 5 years; interest (annual) - 15%; !monthly capitalization! '

'Calculate the amount on the account at the end of the specified period.') 
print ('Answer: The amount = 42143.63 BYN')

print ('To check my solution, as well as to calculate the compound interest using your data, use the form below.')

x = float(input ('Please enter the deposit amount, BYN: \n'))
y = float(input ('Please enter the deposit term, years: \n'))
z = float(input ('Please enter the annual interest rate, % : \n'))
m = y * 12
t = x * (1 + z/100/12) ** m
p = t - x
d = ((p/x)*100)/y

print ('The amount =', round(t,2) , 'BYN' )
print ('Profit =' , round(p,2) ,'BYN')
print ('The yield was (as a percentage per annum):' , round(d,2) , '%')