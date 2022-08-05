import re
from os import system
from time import sleep


# 1) max word lengh to word wrap
with open('start_text.txt','r') as st:
	max_word_len = 0
	string = st.read()
	for i in range(50,1,-1):
		if len(re.findall(r'\w{' + str(i) + '}-', string)) != 0 and len(re.findall(r'\w{' + str(i) + '}-', string)[0]) == i + 1:
			max_word_len = i + 1
			break
		elif len(re.findall(r'\w{' + str(i) + '}', string)) != 0 and len(re.findall(r'\w{' + str(i) + '}', string)[0]) == i:
			max_word_len = i
			break


# 1.5) he-he
scaning = 0
while scaning != 11:
	system('cls||clr')
	print('Searching for a longest word...')
	print('[' + '||' * (1 + scaning) + '  ' * (10 - scaning) + ']')
	scaning += 1
	sleep(0.1)
system('cls||clr')


# 2) user input
#str_len = 30
while True:
	str_len = input(f'Input lengh of string (it must be from 35 symbols, but it also can be from {max_word_len}): ')
	if not str_len.isdecimal():
		print('Error: bad input')
		continue
	elif int(str_len) < max_word_len:
		print('Error: wrong lengh of string')
		continue
	else:
		str_len = int(str_len)
		break

# 3) reading, compiling by width, writing
cursor = 0
new_string = ''
end = False

with open('start_text.txt','r') as st:

	while end != True:

		add_spaces = 0
		st.seek(cursor)
		string = st.read(str_len + 1)

		if string[:-1].count(' ') == 0 and string[:-1].count('-') != 0 and string[len(string)-2] != '-' and  string[len(string)-1] != '\n':
			string = string[:-1][:-string[::-1].index('-') + 1]
			cursor += len(string)
		elif string[:-1].count('\n') == 0 and len(string) == str_len + 1 and string[len(string)-2] not in ' -' and  string[len(string)-1] not in ' \n':
			string = string[:-1][:-string[::-1].index(' ') + 1]
			cursor += len(string)
		elif string[:-1].count('\n') != 0:
			string = string[:-1][:string.index('\n') + 1]
			cursor += len(string) + 1
		elif len(string) != str_len + 1:
			end = True
		else:
			string = string[:-1]
			cursor += str_len

		paragraph = True if string.count('\n') != 0 or end == True else False
			
		string = string.strip()

		if len(string) != str_len:
			add_spaces = str_len - len(string) # spaces to add

		if string.count(' ') != 0:
			all_spaces = add_spaces // string.count(' ') # multiple increase of all spaces in string
			some_spaces = add_spaces % string.count(' ') # increase some spaces in string

		if string.count(' ') != 0 and add_spaces % string.count(' ') == 0 and not paragraph:
			string = string.replace(' ', ' ' * (1 + all_spaces))
		elif string.count(' ') != 0 and not paragraph:
			string = string.replace(' ', ' ' * (1 + all_spaces))
			string = string.replace(' ' * (1 + all_spaces), ' ' * (2 + all_spaces), some_spaces)

		new_string += string + '\n' if end == False else string

with open('my.txt','w') as my:
	my.write(new_string + '\n') if end == False else my.write(new_string)
