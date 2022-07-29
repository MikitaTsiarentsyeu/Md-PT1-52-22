
string = 'one one eighteen thirteen thirteen eight ten twenty eleven fourteen thirteen five three'
print(f'\n{string}')

#>>>>>>>>>> 1) from string to digits
string = string .split()
while string[0] not in range(1,21):
	string.append({'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
			'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
			'eighteen':18,'nineteen':19, 'twenty':20}[string.pop(0)])
print(f'\n1)     {string} <- words to digits')

#>>>>>>>>>> 2), 3) no duplicates, sorted from min to max
string = list(set(string))
print(f'2), 3) {string} <- no duplicates and sorted from min to max', end = '\n4)     ')

#>>>>>>>>>> 4) a*b, b+c, c*d,...
while True:
	if string[1] < 100:
		print(string[0]*string[1], end = ' ')
		string.append(string.pop(0)+100)
	else:
		string.append(string.pop(0)+100)
		break

	if string[1] < 100:
		print(string[0]+string[1], end = ' ')
		string.append(string.pop(0)+100)
	else:
		string.append(string.pop(0)+100)
		break

while string[0] > 100:
	string.append(string.pop(0)-100)
print(' <- 4) a*b, b+c, c*d,... from 2), 3)')

#>>>>>>>>>> 5) sum of odd from 1) 2) 3)
while string[0] < 100:
	if string[0] % 2 != 0:
		string.append(string.pop(0)+100)
	else:
		del string[0]

while string[0] > 100:
	string.append(string.pop(0)-100)

print(f'5)     {sum(string)} <- sum of odd from 2), 3)')
