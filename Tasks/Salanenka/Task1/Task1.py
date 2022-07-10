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
