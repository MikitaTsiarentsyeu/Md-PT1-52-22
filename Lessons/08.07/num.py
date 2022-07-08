import math
import random

print(math.pi, math.e, math.nan, math.inf)

#2/0

math.pow(2, 3) == 2**3
math.sqrt(144) == 144**0.5
print(math.factorial(10))
print(math.log2(8))

print(random.randrange(1, 5))
print(random.randint(10, 12))
print(random.randint(10, 12))
print(random.randint(10, 12))
print(random.randint(0, 1))
print(random.randrange(0, 2))

l = [1,2,3,4,5]
print(random.choice(l))
random.shuffle(l)
print(l)