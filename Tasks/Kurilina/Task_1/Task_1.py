import math


start_depozit = 20000
term_years = 5
count_terms_in_year = 12
interest_rate_year = 0.15

finish_depozit = round(start_depozit * math.pow((1 + interest_rate_year/count_terms_in_year),count_terms_in_year*term_years),2)
print(finish_depozit)



mas = []

def interest_calculation(start_depozit):
    common_term = 60

    if len(mas) < common_term:      
        count_terms_in_year = 12
        interest_rate_year = 0.15 
        start_depozit = round((start_depozit * (1 + interest_rate_year/count_terms_in_year)),2)
        mas.append(start_depozit)
        interest_calculation(start_depozit)
    else:    
        print(mas[common_term-1])
          
interest_calculation(20000)        
        