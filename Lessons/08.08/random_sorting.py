import random

l = [3,2,6,5,4,1,7,8]

def sort(l):
    counter = 0
    while not is_sorted(l):
        counter += 1
        print(counter)
        swap(l)

def swap(l):
    n = len(l)
    i = generate_index(n)
    j = i
    while i == j:
        j = generate_index(n)
    l[i], l[j] = l[j], l[i]

def generate_index(n):
    return random.randrange(0, n)

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True

sort(l)
print(l)