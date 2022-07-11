import math

dep = 20000 
t = 5
per = 15

T = t*12 
Per = per/100
Sum = dep * math.pow(1 + Per/12, T)

print(round(Sum, 2))