s = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'

d = {'five':5, 'thirteen':13, 'two': 2, 'eleven':11, 'seventeen':17, 'two':2, 'one':1, 'thirteen':13, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}

l = list({d[x] for x in s.split()})
print (l)

for i in range (len(l)-1):
    if i%2 == 0:
        print (l[i]*l[(i+1)], end=', ')
    else:
        print (l[i]+l[(i+1)], end=', ') 
print()

l2 = 0
for i in range(len(l)):
    if l[i] % 2 != 0:
        l2 += l[i]
print(l2)
