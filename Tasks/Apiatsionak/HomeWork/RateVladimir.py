#
#Interest rate 15%

print('Hello, to calculate income, select the following type of capitalization:')
print('Interest rate 15%')
a = int(input('Annual - 1 and Monthly - 2''\n'))
b = int(input('What amount will you deposit in BYN''\n'))
c = int(input('How long will you sign the contract in months''\n'))
e = 15/100 #This is a part of the amount invested or already paid together with the invested#
f = c // 12 #This is how many years in 24 months#
z = int(c % 12) #How many months without a year#
#The formula for calculating the annual capitalization for years only! or 12.24.... months
#
d1 =((1+e))**(c/12)*b

#Formula for calculating annual capitalization with year and month or 25, 37 months, etc.
#
d2 = (b * (((1+e))**(f)))*((1+(e*(z/12))))
#Formula for Monthly Capitalization
d3 = b*(1+e/12)**c
#When months are divisible by 12 without a remainder for annual capitalization

if a == 1 and c % 12 == 0 :
    print('Your income together with profit:')
    print(d1)
    print("You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")
#Divided by 12 with remainder for annual capitalization
elif a ==1 and c % 12 != 0 :
    print('Your income together with profit:')
    print(d2)
    print("You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")

elif a == 2:
    print('Your income together with profit:')
    print(d3)
    print("You can look at the formulas and calculate the income on the site yourself on the calculator raiffeisen.ru")
else:
    print('Error')
    print("Please enter correct data")
input('Press enter to exit the program')
#This is necessary because the program runs quickly and we do not see the result.


