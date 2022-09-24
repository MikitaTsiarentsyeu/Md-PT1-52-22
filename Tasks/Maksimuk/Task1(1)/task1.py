import math
import decimal

dep = decimal.Decimal(input("Enter Principal, BYN:\n"))
per = decimal.Decimal(input("Enter Interest Rate, %:\n"))
t = decimal.Decimal(input("Enter Term, years:\n"))

c = int(input("Choose Compounding:\n 1) Monthly\n 2) Annualy\n"))
if c == 1:
   T = t*12 
   Per = per/100
   Sum = dep * decimal.Decimal(math.pow(1 + Per/12, T))
   print("Future value:\n", round(Sum, 2), "BYN")
elif c == 2:
   Per = per/100
   Sum = dep * decimal.Decimal(math.pow(1 + Per, t))
   print("Future value:\n", round(Sum, 2), "BYN")
else:
 print("Invalid input format. Please, try again.\n") 