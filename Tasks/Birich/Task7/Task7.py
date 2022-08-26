def list_sum(list_item):
    if not isinstance(list_item, list):
        return list_item
    return sum(map(list_sum, list_item))


result = list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]])
print(result)


fib_list = [0, 1]


def fib(num):
    if num <= len(fib_list):
        return fib_list[num-1]
    else:
        fib_num = fib(num-1) + fib(num-2)
        if num > len(fib_list):
            fib_list.append(fib_num)
        return fib_num


fib(5)
print(fib_list)
fib(10)
print(fib_list)
