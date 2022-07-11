import decimal, re

def monthly_capitalization_calculate(p,n,r):
    summ = round((decimal.Decimal(p) * pow((1 + decimal.Decimal(r) / (100 * 12)),(decimal.Decimal(n) * 12))),2)
    print(f'Через {n} лет на счету будет {summ} BYN')

print(f' Банк "Надурим & Co" предлагает Вам открыть депозит с годовой процентной ставкой 15% и ежемесячной капитализацией.\
\nВведите сумму в белке :')
deposit = input().replace(',', '.')
deposit = re.sub ('[^\d.]', "", deposit)

print(f'На сколько лет депозит?')
years_amount = input().replace(',', '.')
years_amount = re.sub ('[^\d.]', "", years_amount)

annual_interest_rate = '15'

monthly_capitalization_calculate(deposit,years_amount,annual_interest_rate)






    

    
