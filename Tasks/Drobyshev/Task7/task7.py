# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34


def sum_all(l):
    total = 0
    for i in l:
        if (type(i) == type([])):
            total = total + sum_all(i)
        else:
            total = total + i
    return total
print("cумма элементов -", sum_all([1, 2, [2, 4, [[7, 8], 4, 6]]]))


# 2. Написать рекурсивную функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def fib(n):
    def fib_num(n):
        if n <= 1:
            return n  
        else:
            return fib_num(n-1) + fib_num(n-2)
    return ','.join([str(fib_num(i)) for i in range(n)])

print(fib(5))
print(fib(10))