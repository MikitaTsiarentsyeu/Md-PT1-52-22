import decimal


a = decimal.Decimal(input("Deposit amount:\n")) 
b = decimal.Decimal(input('Years amount:\n'))
c = decimal.Decimal(input('Procent:\n'))
x=a*((1+b/100/12)**(c*12))
print (round(x,2))
