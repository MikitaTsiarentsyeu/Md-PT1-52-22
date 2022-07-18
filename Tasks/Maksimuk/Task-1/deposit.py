deposit = float(input("Enter initial deposit sum in BYN:\n"))
rate = float(input("Enter interest rate:\n"))
term = float(input("Enter term in years:\n"))
capital = str(input("Choose type of capitalization(write 'years' or 'month':\n"))
if capital == 'month':
    dep_month = deposit*((1+rate/100/12)**(term*12))
    print(dep_month)
elif capital == 'years':
    dep_years = deposit*(1+(rate/100*term))
    print(dep_years) 
else:
    print('Error, please check your input!')