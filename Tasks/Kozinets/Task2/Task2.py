d_b = {9103976271:[('Reina', 'Meinhard'),('Memphis','Tennessee')],
		4199392609:[('Stephanie', 'Bruice'),('Greensboro','North Carolina')],
		9099459979:[('Ermes', 'Angela'),('Dallas','Texas')],
		6123479367:[('Lorenza', 'Takuya'),('Indianapolis','Indiana')],
		7548993768:[('Margarete', 'Quintin'),('Raleigh','North Carolina')]}

#num = '7548993768'
num = input('Enter phone number: ').replace(' ','').replace('-','')

if not num.isdecimal():
    	print('\n[Error: must be only numbers]')
elif len(num) != 10:
    	print('\n[Error: must be only 10 numbers]')
elif int(num) not in d_b:
    	print('\nThe number is not found')
else:
	num = int(num)
	print(f'\n{d_b[num][0][0]} {d_b[num][0][1]} from {d_b[num][1][0]}, {d_b[num][1][1]}')


input()