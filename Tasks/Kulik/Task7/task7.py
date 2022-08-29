def sum (list):
    c = 0
    for i in list:
        if type (i) == type([]):
            c = c + sum(i)
        else:
            c = c + i
    return c

print (sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))

def fib (n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
print(*[fib(i) for i in range(5)], sep = ', ')
print(*[fib(i) for i in range(10)], sep = ', ')



      
