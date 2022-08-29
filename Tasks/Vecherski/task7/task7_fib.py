def fib_last(n):
    if n == 1:
        x = 0
    elif n == 2:
        x = 1
    else:
        x = fib_last(n - 1) + fib_last(n - 2)
    return x

def fib(n):
    l = []
    for i in range(1, n+1):
        l.append(fib_last(i))
    print(*l, sep = ", ")

count = int(input("how many fibonacci numbers to show?\n"))
fib(count)