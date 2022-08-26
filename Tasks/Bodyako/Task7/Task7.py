def sum(list):
    counter = 0
    for i in list:
        if (type(i) == type([])):
            counter = counter + sum(i)
        else:
           counter = counter + i
    return counter
print(f'Sum of items: {sum([1, 2, [2, 4, [[7, 8], 4, 6]]])}')


def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))
n = 5
list = []
for i in range(0, n):
	list.append(fibonacci(i))	
print(*list, sep = ',')


