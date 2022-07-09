import math
print ('In our DROB-Bank you will get the best deposit offer, check it yourself by entering the initial data below.')

x = int(input ('Please enter the deposit amount, BYN: \n'))
y = int(input ('Please enter the deposit term, years: \n'))
z = float(input ('Please enter the annual interest rate, % : \n'))
m = y * 12
t = x * (1 + z/100/12) ** m
p = t - x
d = ((p/x)*100)/y

print ('The amount =', int(t) , 'BYN' )
print ('Profit =' , int(p) ,'BYN')
print ('The yield was (as a percentage per annum):' , round(d,2) , '%')