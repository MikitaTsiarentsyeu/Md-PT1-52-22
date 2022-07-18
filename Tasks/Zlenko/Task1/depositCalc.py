interestRates = [5, 10, 15, 20]
years = [1, 3, 5, 10]
periods = [1, 3, 12]

principalAmount = int(input("Please enter your initial deposit amount:"))
userInterestRate = int(input(f"Please select annual interest % rate from the list {interestRates}:"))/100
userYears = int(input(f"Please select a number of years to keep the deposit in the bank {years}:"))
userPeriods = int(input(f"Please select a number of compound interest periods per year {periods}:"))

finalAmount = principalAmount*(1+userInterestRate/userPeriods)**(userYears*userPeriods)

print(f"Here's the amount you will get in {userYears} year(s): {round(finalAmount, 2)}") 
