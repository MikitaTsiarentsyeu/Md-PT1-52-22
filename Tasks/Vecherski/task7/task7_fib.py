def fib(n):
    x = n if n <= 1 else fib(n-1) + fib(n-2)
    return x

count = int(input("how many fibonacci numbers to show?\n"))
print(*[fib(i) for i in range(count)], sep = ', ')