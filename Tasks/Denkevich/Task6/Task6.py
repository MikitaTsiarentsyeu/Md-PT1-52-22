# My realizations (using only my knowledge)

# Implementation 1:
l = [i for i in range(1, 101)]
la = []
for i in l:
    if i % 3 == 0 and i % 5 == 0:
        la.append('FizzBuzz')
    elif i % 3 == 0:
        la.append('Fizz')
    elif i % 5 == 0:
        la.append('Buzz')
    else:
        la.append(f'{i}')
s = ', '.join(la)
# print(s)
print("-----------------------")

# Implementation 2:
print(", ".join([str(i) if i % 3 != 0 and i % 5 != 0 else 'FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' for i in range(1, 101)]))
print("-----------------------")

# Implementation 3:
import time
def FizzBuzz(s,i):
    n = 1
    while n <= i:
        time.sleep(0.2)
        print(s if n % 3 == 0 and n % 5 == 0 else s[0:4] if n % 3 == 0 else s[4:] if n % 5 == 0 else n)
        n += 1
FizzBuzz('FizzBuzz', 100)

# Implementation 4:
def FizzBuzz():
    s = 'FizzBuzz'
    print([i if i % 3 != 0 and i % 5 != 0 else s if i % 3 == 0  and i % 5 == 0 else s[0:4] if i % 3 == 0 else s[4:] for i in range(1,101)])
FizzBuzz()

# Implementation 5:
def FizzBuzz(f, b):
    print([f"{f}{b}" if i % 3 == 0 and i % 5 == 0 else f if i % 3 == 0 else b if i % 5 == 0 else i for i in range(1, 101)])
FizzBuzz('Fizz', 'Buzz')

# Implementation found in the internet:
# Implementation 6:
s = ''
for i in range(1, 101):
    if i % 3 == 0:
        s += 'Fizz'
    if i % 5 == 0:
        s += 'Buzz'
    if i % 3 != 0 and i % 5 != 0:
        s += str(f" {i} ")
print(s)

# Implementation 7:
l = []
for i in range(1, 101):
    if i % 15 == 0:
        l.append('FizzBuzz')
    elif i%3 == 0:
        l.append('Fizz')
    elif i%5 == 0:
        l.append('Buzz')
    else:
        l.append(i)
print(l)

# And Implementation 8.
# The most butiful realization I found!
print(*('FizzBuzz'[(0,4,4)[x % 3]:4 if x % 5 else 8] or x for x in range(1,101)))
# I spent lots of time to realise this logic and it impressed me greatly.
# First I didn't know that -1 returns True as it does 1 (I guess I listened the lectures not very well).
# Second I rethought the operation with devision remainder: this cortage includes 3 values while its indexes plays role the devision remainders. It's realy cool.
# Third I admired the whole logic in "split" method. And I never know about that there is can be choice in appending valubles in the comprehension (generator in this case). I talk about "or" operator: comprehension choose x instead "" that we have in a case "FizzBuzz"[4:4]. . 
# There is so many simple constructions wich work in difficult logic in this implementation.
# My implementations look so mediocre now. Bou it's okay I think. =)
# And fourth my Eanglish much to be desired.

# Implementation 9 (It's my implementation on a basis of prevoios):
l = []
s = "FizzBuzz"
for i in range(1, 101):
    if i % 3 == 0:
        l.append(s[0:4 if i % 5 != 0 else 8]) # It's realy usefull aproach.
    elif i % 5 == 0:
        l.append(s[4:])
    else:
        l.append(i)
print(*(l))