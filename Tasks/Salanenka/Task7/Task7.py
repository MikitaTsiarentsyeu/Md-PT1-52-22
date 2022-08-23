def summa (a):
    sum=0
    for i in a:
        if type(i) == int:
            sum+=i
        if type(i) == list:
            sum+=summa (i)
    return sum

d = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print (summa(d))

def fib(n):
    def fi (n):
        if n<=1: 
            return n
        return (fi(n-1)+fi(n-2))
    print (*[fi (i) for i in range (n)], sep=', ')

(fib(5))
(fib(10))


