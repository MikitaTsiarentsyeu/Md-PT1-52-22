# Task 7.1 Sum of the list elements and other included lists elements:


def sum_el(l):
    s = 0
    for i in l:
        if isinstance(i, list):
            s += sum_el(i)
        else:
            s += i
    return s


l = [1, [2, 7, 10], [3, 4, [5, 6, [7, 8], 9, 10]]]
print(sum_el(l))


# Task 7.2.1 Function of Fibonacci numbers:


print('-----------')
def fib(n, a = 0, b = 0, c = 1):
    if n == 0:
        print("There is no Fibonachi numbers.")
    elif n == 1:
        print(f"{a}", end = '.')
        return print()
    else:
        print(f"{a}, ", end = '')
        if n > 1:
            a = b + c
            fib(n-1, a = a, b = a, c = b)
    

fib(6)


# Task 7.2.2 The same with the list:


def fib(n, a = 0, b = 0, c = 1, l = []):
    if a == 0:
        l.append(a)
    if n == 1 or n == 0:
        return print(f"{', '.join(map(str, l))}.")
    if n > 1:
        a = b + c
        l.append(a)
        return fib(n-1, a = a, b = a, c = b, l = l)
    

fib(7)


# Task 7.2.3 Improving solution with cycle:


def fib(n, a = 1, l = [0,1]):
    if n == 1:
        return l[0]
    if a == n - 1:
        return print(", ".join(map(str, l)))
    else:
        for i in range(a, a + 1):
            l.append(l[i-1] + l[i])
            return fib(n, a + 1, l = l)


fib(8)


# Task 7.2.4 It's the best solution I can make at the moment:


def fib(n, a = 0, b = 1, l = []):
    if n == 0:
        return print(", ".join(map(str, l)))
    else:
        b += a
        l.append(a)
        return fib(n - 1, a = b, b = a , l = l)


fib(9)