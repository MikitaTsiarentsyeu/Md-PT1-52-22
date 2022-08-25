def sum(list):
    total = 0
    for i in list:
        if (type(i) == type([])):
            total = total + sum(i)
        else:
            total = total + i
    return total
print("Sum of elements is -", sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
   
print (*[fibonacci(i) for i in range(5)], sep = ',')
print (*[fibonacci(i) for i in range(10)], sep = ',')


