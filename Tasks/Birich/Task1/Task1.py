
import decimal


present_value = 20000
year = 5
month = 12
interest_rate = 15

result_rate = decimal.Decimal(interest_rate / 100)  # conversion of interest

result_value = present_value * ((1 + result_rate / month) ** (month * year))

print(result_value, 'BYN')
