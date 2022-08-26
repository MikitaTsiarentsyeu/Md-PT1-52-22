def rec_sum(l):
    s = 0
    for i in l:
        if type(i) == list:
            s += rec_sum(i)
        else:
            s += i
    return s

l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(rec_sum(l))

def fib(n):
    if n <= 1 :
        return n
    else:
        return(fib(n-1) + fib(n-2))

print(*[fib(i) for i in range(5)], sep = ', ')
print(*[fib(i) for i in range(10)], sep = ', ')