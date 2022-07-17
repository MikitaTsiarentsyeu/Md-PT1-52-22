import math

start_depozit = int(input('Please, enter start depozit:\n'))#20000
term_years = int(input('Please, enter deposit term, years:\n'))#5
count_terms_in_year = int(input('Please, enter the desired frequency of capitalization (every month - 12, every quarter - 4, once a year - 1):\n'))#12
interest_rate_year = int(input('Please, enter annual interest rate, %:\n')) / 100 #0.15

finish_depozit = round(start_depozit * math.pow((1 + interest_rate_year/count_terms_in_year),count_terms_in_year*term_years),2)
print(f'Your deposit at the end of the term will be: {finish_depozit},  accumulated profit: {round(finish_depozit-start_depozit,2)}')