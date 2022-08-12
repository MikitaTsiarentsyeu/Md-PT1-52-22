# Task 5.1
str = 'The quick Brown Fox'


def check_str(s):
    up = 0
    low = 0
    s = s.replace(' ','')
    for i in range(len(s)):
        if s[i].isupper():
            up += 1
        else:
            low += 1
    return print(f'{up} upper case, {low} lower case')


check_str(str)

# Task 5.2


def is_prime(n):
    if n <= 0:
        print('Incorrect number. Please inpot number greater than or equel to 0.')
    else:
        if n == 1:
            return True
        elif n == 2:
            return False
        elif n > 2:
            for i in range(2, n):
                if n % i == 0:
                    return False
            else:
                return True


print(is_prime(787))
print(is_prime(777))

# Task 5.3


def get_ranges(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] == l[i]:
                print(
                    'There are dublicates in this list. Please input a list without dublicates.')
                return
    for i in l:
        if i != 0 and not isinstance(i, int):
            return print('There are not integer values in this list. Please input integer values.')
    for i in range(len(l) - 1):
        if l[i+1] >= l[i]:
            continue
        else:
            return print("Numbers in the list aren't arranged in the ascending order. Please arrange it in correct order.")
    else:
        start = 0
        str = ''
        for i in range(len(l)):
            if i >= len(l) - 1:
                if start != i:
                    str += f'{l[start]}-{l[i]}'
                else:
                    str += f'{l[i]}'
            elif l[i] + 1 != l[i + 1]:
                if start != i:
                    str += f'{l[start]}-{l[i]}, '
                    start = i + 1
                else:
                    str += f'{l[i]}, '
                    start = i + 1
    return print(str.strip(' '))


get_ranges([0, 1, 2, 2, 3, 7, 8, 10, 10])  # Dublicates
get_ranges([0, 1, 2, 2.3, 3, 7, 8, 10])  # Float
get_ranges([0, 1, 2, 5, 6, 7, 19, 18, 17])  # Incorrect order
get_ranges([0, 1, 2, 3, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
