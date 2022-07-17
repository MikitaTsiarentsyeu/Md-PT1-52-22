from decimal import Decimal as Dec


print('\n' + ' '*25,end = '')
print('>>DEPOSIT CALCULATION<<\n')

while True:
	try:
		deposit = Dec(input('\n 1/4) Enter the deposit amount, BYN: '))
	except Exception:
		print(' [Error: Must be a number]')
		continue
	if deposit <= 0:
		print(' [Error: Must be a positive number]')
		continue
	break


while True:
	try:
		rate = Dec(input('\n 2/4) Enter the interest rate, %: '))
	except Exception:
		print(' [Error: Must be a number]')
		continue
	if rate <= 0:
		print(' [Error: Must be a positive number]')
		continue
	break


while True:
	try:
		cap_period = int(input('\n 3/4) Enter the period of capitalisation (1,3,6 or 12), months: '))
	except Exception:
		print(' [Error: Must be a number]')
		continue
	if cap_period not in (1,3,6,12):
		print(' [Error: Invalid input format]')
		continue
	break


while True:
	term = input('\n 4/4) Enter the deposit term (example: 5/0, 2/6, 3/11), years/months: ')
	try:
		term_y = int(term.split('/')[0])
	except Exception:
		print(' [Error: Invalid input format]')
		continue
	try:
		term_m = int(term.split('/')[1])
	except Exception:
		print(' [Error: Invalid input format]')
		continue
	if term_m >= 12:
		print(' [Error: Number of month must be from 0 to 11]')
		continue
	if term_y < 0 or term_m < 0:
		print(' [Error: Must be a positive number]')
		continue
	if term_m % cap_period != 0:
		print('\n\n [Warning: There is no final capitalisation in the end of the deposit term]')
	break


profit = round(deposit * (1 + rate * Dec('0.01'))**(term_y + Dec(str((term_m // cap_period)/12))),2)

print(f'\n\n Your final amount will be {profit} BYN')

input()