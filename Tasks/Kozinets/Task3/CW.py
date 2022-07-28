d_b = {'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
		'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,
		'seventeen':17,'eighteen':18,'nineteen':19, 'twenty':20}

string = 'one one eighteen thirteen thirteen eight ten eleven'
print(string)

a = list({d_b[i] for i in string.split()})
print(f'1), 2), 3) {a} <- words to digits, no duplicates, sotred from min to max')

b = [a[i]*a[i+1] if i%2 == 0 else a[i]+a[i+1] for i in range(len(a)-1)]
print(f'4)         {b} <- a*b, b+c, c*d, d+e, ... from 1), 2), 3)')

c = sum([i for i in a if i%2 != 0])
print(f'5)         {c} <- sum of odd from from 1), 2), 3)')