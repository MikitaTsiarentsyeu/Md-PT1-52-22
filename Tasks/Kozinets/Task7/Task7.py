a = [1,2,[2,4,[[7,8],4],6],[1,2,[2,4,[[7,8],4],6]]] #<- 68

def list_sum(l):
	j = 0
	for i in l:
		j += list_sum(i) if isinstance(i,list) else i
	return j


def fib_1(n): #return list of integers
	if n != 1:
		j = fib_1(n-1)
		j.append(1) if n == 2 else j.append(j[-1] + j[-2])
		return j
	else:
		return [0]


def fib_2(n): #return list of strings
	if n != 1:
		j = fib_2(n-1)
		j.append('1') if n == 2 else j.append(str(int(j[-1]) + int(j[-2])))
		return j
	else:
		return ['0']


def fib_3(n): #shortest way
	if n != 1:
		j = fib_3(n-1)
		return j + [1] if n == 2 else j + [j[-1] + j[-2]]
	else:
		return [0]


def fib_4(n): #the_dich
	if n != 1:
		return fib_4(n - 1) + [1] if n == 2 else fib_4(n-1) + [fib_4(n-1)[-1] + fib_4(n-1)[-2]]
	else:
		return [0]

def fib_5(n): #the_dich_V2
	return fib_5(n-1) + [1] if n == 2 else fib_5(n-1) + [fib_5(n-1)[-1] + fib_5(n-1)[-2]] if n != 1 else [0]



print(list_sum(a))
print(', '.join(list(map(str,fib_1(9)))))
print(', '.join(fib_2(9)))
print(*fib_3(9), sep = ', ')
print(fib_4(9))
print(fib_5(9))

