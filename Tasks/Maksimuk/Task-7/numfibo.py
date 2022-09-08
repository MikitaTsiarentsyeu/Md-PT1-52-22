def sumlist (a):
    sum=0
    for i in a:
        if type(i) == int:
            sum+=i
        if type(i) == list:
            sum+=sumlist (i)
    return sum

d = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print (sumlist(d))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter the number of items in Fibonacci series:"))
for i in range(n):
    print(fibonacci(i), end = ',')