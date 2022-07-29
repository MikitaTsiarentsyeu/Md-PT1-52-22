s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
d = {'five': 5, 'thirteen': 13, 'two':2, 'eleven': 11, 'seventeen':17, 'one':1, 'ten':10, 'four':4, 'eight':8, 'five':5, 'nineteen':19}
l = list({d[x] for x in s.split()})
print (l)

for i in range (len(l)-1):
    if i%2 == 0:
        print (l[i]*l[(i+1)])
    else:
        print (l[i]+l[(i+1)])

sum = 0 
for i in range (len(l)):
    if l[i]%2 != 0:
        sum +=l[i]
print (f'Сумма нечетных чисел:{sum}')
