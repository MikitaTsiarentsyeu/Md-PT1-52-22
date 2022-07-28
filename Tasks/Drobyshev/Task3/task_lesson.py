# this solution uses 2 variables
"five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
а = list(set({'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}.values()))
print(а)
for a in range (len(а)-1):
    print (а[a]*а[a+1], end="  ") if a%2 == 0 else print (а[a]+а[a+1], end="  ")
print()
print(f"The total sum of all odd numbers = {sum(а for а in а if а%2 !=0)}")



# this solution uses 1 variable
import math
"five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
a = list(set({'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}.values()))
print(a)
print(f"{math.prod(a for a in a[(len(a)-len(a)):(len(a)-len(a)+2)])}", end="  ")
print(f"{sum(a for a in a[(len(a)-len(a)+1):(len(a)-len(a)+3)])}", end="  ")
print(f"{math.prod(a for a in a[(len(a)-len(a)+2):(len(a)-len(a)+4)])}", end="  ")
print(f"{sum(a for a in a[(len(a)-len(a)+3):(len(a)-len(a)+5)])}", end="  ")
print(f"{math.prod(a for a in a[(len(a)-len(a)+4):(len(a)-len(a)+6)])}", end="  ")
print(f"{sum(a for a in a[(len(a)-len(a)+5):(len(a)-len(a)+7)])}", end="  ")
print(f"{math.prod(a for a in a[(len(a)-len(a)+6):(len(a)-len(a)+8)])}", end="  ")
print(f"{sum(a for a in a[(len(a)-len(a)+7):(len(a)-len(a)+9)])}", end="  ")
print(f"{math.prod(a for a in a[(len(a)-len(a)+8):len(a)])}", end="  ")
print()
print(f"The total sum of all odd numbers = {sum(a for a in a if a%2 !=0)}")