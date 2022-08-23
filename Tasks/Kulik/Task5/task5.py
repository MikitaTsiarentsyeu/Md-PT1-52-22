def check_str(a):
    upper = 0
    lower = 0
    for i in a:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
    return f'{a} -> {upper} upper case, {lower} lower case'        

print(check_str('The quick Brown Fox'))    

def is_prime(b):
    k = 0
    for i in range(2, b // 2 + 1):
        if (b % i == 0): 
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False

print(is_prime(787))
print(is_prime(777))

def get_ranges(c):
    list = []
    for i in c:
        if i != c[0] + 1:
            list.append([i])
        elif len(list[-1]) > 1:
            list[-1][-1] = i
        else:
            list[-1].append(i)
        c[0] = i
    return (', '.join(['-'.join(map(str, part)) for part in list]))

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))