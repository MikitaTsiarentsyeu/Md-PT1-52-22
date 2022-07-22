import random
l = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(l)
print(l)
sorted_l = sorted(l)
print(sorted_l, l)
l.sort()
print(l)

random.shuffle(l)

for j in range(len(l)-1):
    for i in range(len(l)-1):
        if (l[i]>l[i+1]):
            l[i+1], l[i] = l[i], l[i+1]
    print(l)