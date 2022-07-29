import random

# Сonditions:
# -----------

s ='five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

# Solutions:
# ----------

print('\n')

# 1
print('1. Just figures:')
d = {5: 'five', 13: 'thirteen', 2: 'two', 11: 'eleven', 17: 'seventeen', 1: 'one',
     10: 'ten', 4: 'four', 8: 'eight', 19: 'nineteen'}
l2 = []
for j in range(len(list(s.split(' ')))):
    for i, e in d.items():
        if list(s.split(' '))[j] == e:
            l2.append(i)
            break
print(l2)

#2
print('2. No dublicates:')
print(set(l2))

#3
print('3. Sorting:')
l4 = list(set(l2))
random.shuffle(l4)
print('Shuffled:')
print(l4)
for i in range(len(l4)):
    for j in range(len(l4)):
        if l4[j] > l4[i]:
            l4[j], l4[i] =  l4[i], l4[j]
print('Sorted:')
print(l4)

#4
print('4. Some calculating:')
b = l4
l3 = []
flag = True
i = 0
while i in range(len(b) - 1):
    if flag == True:
        l3.append(b[i]+b[i+1])
        flag = not flag
        i += 2
        continue
    if flag == False:
        l3.append(int(b[i])*int(b[i+1]))
        flag = not flag
        i += 2
        continue
print(l3)

#5
print('5. The summ of odd numbers:')
sum = 0
for i in range(len(b)):
    if b[i] % 2 != 0:
        sum += b[i]
print(sum)