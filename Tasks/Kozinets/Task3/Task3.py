from datetime import datetime
from time import sleep
from os import system

#	   hour[0]			hours[1]		minute[2]		minutes[3]
ru = {0:('',			'',				'',				'ровно'),
	1:('один',			'первого',		'одна',			'одной'),
	2:('два',			'второго',		'две',			'двух'),
	3:('три',			'третьего',		'три',			'трех'),
	4:('четыре',		'четвертого',	'четыре',		'четырех'),
	5:('пять',			'пятого',		'пять',			'пяти'),
	6:('шесть',			'шестого',		'шесть',		'шести'),
	7:('семь',			'седьмого',		'семь',			'семи'),
	8:('восемь',		'восьмого',		'восемь',		'восьми'),
	9:('девять',		'девятого',		'девять',		'девяти'),
	10:('десять',		'десятого',		'десять',		'десяти'),
	11:('одинадцать',	'одинадцатого',	'одинадцать',	'одинадцати'),
	12:('двенадцать',	'двенадцатого',	'двенадцать',	'двенадцати'),
	13:('',				'',				'тринадцать',	'тринадцати'),
	14:('',				'',				'четырнадцать',	'четырнадцати'),
	15:('',				'',				'пятнадцать',	'пятнадцати'),
	16:('',				'',				'шестнадцать'),
	17:('',				'',				'семнадцать'),
	18:('',				'',				'восемнадцать'),
	19:('',				'',				'девятнадцать'),
	20:('',				'',				'двадцать'),
	30:('',				'',				'тридцать'),
	40:('',				'',				'сорок'),
	50:('',				'',				'пятьдесят'),
	'h':('час ',	'часа ',	'часов '),
	'm':('минута',	'минуты',	'минут'),
	's':('секунда',	'секунды',	'секунд')}

time = ''
hours = ''
minutes = ''
seconds = ''


while True:

	request = input('Введите время вручную в формате ЧЧ:ММ, или \n'
					'нажмите ENTER, что бы узнать время компьютера: ')

	if  request == '':
		time = [int(i) for i in str(datetime.now()).replace('-','').replace('.',' ').split(' ')[1].split(':')]
		system('cls||clr')
		break
	elif ':' not in request or len(request) != 5 or not request[:2].isdecimal() or not request[3:].isdecimal():
		system('cls||clr')
		print('Ошибка: Неверный формат времени\n')
		continue
	else:
		time = [int(i) for i in request.split(':')]
		time.append(0)
		print('')
		break

while True:

	if time[0] > 12:
		time[0] = time[0] % 12


	if time[0] == 1:
		hours = ru['h'][0]
	elif time[0] in [2,3,4]:
		hours = ru['h'][1]
	else:
		hours = ru['h'][2]


	if time[1] in [1,21,31,41]:
		minutes = ru['m'][0]
	elif time[1] in [2,3,4,22,23,24,32,33,34,42,43,44,59]:
		minutes = ru['m'][1]
	else:
		minutes = ru['m'][2]


	if time[2] in [1,21,31,41,51]:
		seconds = ru['s'][0]
	elif time[2] in [2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]:
		seconds = ru['s'][1]
	else:
		seconds = ru['s'][2]


	flag = 1 if time[1] < 20 else 0

	if time[1] not in [0,30] and time[1] not in range(45,60):
		print(f'\nСейчас {ru[time[0]][0]} {hours} {ru[(10*(time[1]//10)) + flag*(time[1]%10)][2]} {ru[(1-flag)*time[1] % 10][2]} {minutes}', end = '')
	elif time[1] == 0:
		print(f'\nСейчас {ru[time[0]][0]} {hours} {ru[time[1]][3]}', end = '')
	elif time[1] == 30:
		print(f'\nСейчас половина {ru[time[0] % 12 + 1][1]}', end = '')
	else:
		print(f'\nСейчас без {ru[60 - time[1]][3]} {minutes} {ru[time[0]%12 + 1][0]}', end = '')

	if request != '':
		break

	if time[2] in range(1,21) or time[2] in [30, 40, 50]:
		print(f' и {ru[time[2]][2]} {seconds}')
	elif time[2] in range(20,60):
		print(f' и {ru[10*(time[2] // 10)][2]} {ru[time[2]%10][2]} {seconds}')
	elif time[2] == 0:
		print('')

	sleep(0.2)

	time = [int(i) for i in str(datetime.now()).replace('-','').replace('.',' ').split(' ')[1].split(':')]
	system('cls||clr')

input()