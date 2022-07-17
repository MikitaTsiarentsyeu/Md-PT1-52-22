
deposit = int (input ('Enter the amount of deposit: \n'))
rate = int (input ('Enter the interest rate in percent per year: \n'))/100
term = int (input ('Enter the time period in years: \n'))
capitalization = input ('Press 1 for monthly capitalization and press 2 for yearly capitalization: \n')
print (capitalization)
valueMonthly = deposit*(1+rate/12)**(term*12)
valueYearly = deposit*(1+rate)**term

if capitalization == '1':
    print (f'Your total value in {term} years with monthly capitalization will be: {round(valueMonthly, 2)} BYN')
elif capitalization == '2':
    print (f'Your total value in {term} years with yearly capitalization will be: {round(valueYearly, 2)} BYN')
else:
    print ('Error. Please try again.')


#1 вариант
deposit = 20000
term = 5*12
rate = 15/100/12
newDeposit = deposit*(1+rate)**term
print (round(newDeposit, 2),'BYN')

#2 вариант
deposit = 20000
term = 5*12
rate = 15/100/12
i = 0
for i in range (term):
    deposit = deposit*(1+rate)
    i+=1
print (round(deposit, 2),'BYN')

#3 вариант
deposit = 20000
rate = 15/100/12
term = 5*12
i = 1
while i<=term:
    deposit = deposit*(1+rate)
    i+=1
print (round (deposit, 2),'BYN')

#вариант 1 - самый короткий и быстрый, варианты 2 и 3 можно использовать, если нужно будет выводить на печать накопленные % за каждый месяц переносом print в тело цикла