def sum(l):
    res = 0
    for item in l:
        if type(item) == type([]):
            res = res + sum(item)
        else:
            res = res + item
    return res 

print (sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))               

def fib(n):
    if n<= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = int(input("Enter the number\n"))   
for i in range(n):
    print(fib(i))   
         