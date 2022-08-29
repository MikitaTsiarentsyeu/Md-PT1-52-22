1
def check_str(a):

    if len(a) > 0:
        b = {'upper_case': 0, 'lower_case': 0}
        for a in a:
            if a.islower():
                b['lower_case'] += 1
            elif a.isupper():
                b['upper_case'] += 1

    return print(b['upper_case'], 'upper case', b['lower_case'], 'lower case')
check_str('The quick Brown Fox')

2
def  fact(a):
    fact = 1
    i = 0
    while i < a:
        i += 1
        fact = fact * i
    return fact
# Wilson's theorem
def is_prime(a):
    if (fact(a-1)+1) % a != 0:
        print (False)
    elif a < 2:
        print(False)
    else:
        print(True)
    return
is_prime(787)
is_prime(777)

3
def get_ranges(a):
    if a == []:
        print('Enter a list of non-repeating numbers')
    b = sorted(list(a))
    v = {x for x in a if b.count(x)>1}
    v = sorted(v)
    l = sorted(v)
    num = 0
    sch = []
    if l == v and l != []:
        print('Enter a list of non-repeating numbers')
    if v == []:

        for i in range(len(a)):
            if i != len(a) - 1 and int(a[i] + 1) == a[i + 1]:
                num += 1
            elif num == 0:
                sch.append(str(a[i]))
            else:
                sch.append(f'{a[i - num]}-{a[i]}')
                num = 0
    return ', '.join(sch)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
print(get_ranges([]))
