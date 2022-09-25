#1
def listsummer(listitem):
    if not isinstance(listitem, list):
        return listitem
    return sum(map(listsummer, listitem))


resultat = listsummer([1, 2, [2, 4, [[7, 8], 4, 6]]])
print(resultat)

#2
fibonaccilist = [0, 1]


def fibo(num):
    if num <= len(fibonaccilist):
        return fibonaccilist[num-1]
    else:
        fib_nummer = fibo(num-1) + fibo(num-2)
        if num > len(fibonaccilist):
            fibonaccilist.append(fib_nummer)
        return fib_nummer

fibo(5)
print(fibonaccilist)
fibo(10)
print(fibonaccilist)