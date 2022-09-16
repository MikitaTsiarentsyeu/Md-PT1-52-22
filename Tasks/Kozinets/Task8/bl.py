import data
from os import system
from time import sleep
from decimal import Decimal
from random import randint




cart = [	]




#######################################################################  start
def represent_category():
	"""takes nothing, returns list of names (keys) of items from choosen category"""

	def category_data_keys(category:str):
		for dict in data.db:
			for key in dict:
				if dict[key][0] == category:
					return sorted(dict)

	while True:
		clear()
		print('[0] [< exit]\n===============\nChoose category :')
		n = 1
		category_list = []

		for dicts in data.db:
			for key in dicts:
				if key == 'name:': continue
				category_list.append(dicts[key][0])
				break

		category_list = sorted(category_list)
		for i in category_list:
			print(str([n]) + (' ' * (5 - len(str(n))))  + i)
			n += 1

		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(n):
			if response == '0':
				return 'exit'
			else:
				return category_data_keys(category_list[int(response) - 1])
		else:
			bad_input()
			continue
#######################################################################  start

#######################################################################  catalog

def represent_table(category_data_keys):
	"""take list of names, display data"""
	#print table with items
	def data_cell(item,width_of_column):
		return ' ' + item + ' ' * (width_of_column - len(item)-2) + '|'

	data_base = data_from_keys(category_data_keys)
	max_value = [] #max values lengths from all chosen category data keys


	for key in data_base: #counting lengh of items attributes ##ok
		if key == 'name:': continue
		length_of_attribute_value = [len(key)]
		for value in data_base[key]:
			length_of_attribute_value.append(len(value))
		max_value.append(length_of_attribute_value)


	for j in range(1,len(max_value)): #choose max of lengh of items attributes ##ok
		for k in range(len(max_value[j])):
			if max_value[j][k] > max_value[0][k]:
				max_value[0][k] = max_value[j][k]

	max_value = max_value[0] #left only max lenghs ## ok

	word_from_max_value = 1
	head_strings_num = 2

	for value in data_base[category_data_keys[-1]]: #numbers of words attribute name  ## ok
		if value.count(' ') + 1 > head_strings_num and value != 'quantity in stock':
			head_strings_num = value.count(' ') + 1


	head = [['  #  |' if string == 0 else '     |' for string in range(head_strings_num)]] #building a hight of head? where an element is a string## ok

	head.append([' name' + (' ' * (max_value[0] - 4)) + ' |' if string == 0 else (' ' * max_value[0]) + '  |' for string in range(head_strings_num)])

	for	attribute in data_base[category_data_keys[-1]]: #creating list of strings of head
		if attribute == 'quantity in stock':
			head.append([' quantity |',' in stock |'] + ['          |' for string in range(head_strings_num) if string > 1]  )
		else:
			width = max(max_value[word_from_max_value], max(list(map(len,attribute.split()))))

			if len(attribute.split()) == 1:
				head.append([' ' + attribute + (' ' * (width - len(attribute))) + ' |' if string == 0 else (' ' * width) + '  |' for string in range(head_strings_num)])

			if len(attribute.split()) > 1:
				head.append([' ' + attribute.split()[string] + (' ' * (width - len(attribute.split()[string]))) + ' |' if string + 1 <= len(attribute.split()) else (' ' * width) + '  |' for string in range(head_strings_num)])
				           #f' {description.split()[string]}{' ' * (width - len(description.split()[string]))} |'                                                         f'{' '* width} |'
		word_from_max_value += 1

	widh_of_column = []

	#print(*['\n[',category_data_keys[-1].replace('_name_:',''), ']'],sep = '')
	for i in head:
		print('_' * len(i[1]), end = '')

	for i in range(head_strings_num):  #printing head of selected items
		print()
		for j in head:
			if i == head_strings_num - 1:
				widh_of_column.append(len(j[i]))
				print(j[i].replace(' ','_'),end = '')
			else:
				print(j[i],end = '')
	print()

	N_of_item = 1
	for item in category_data_keys: #print selected items
		if item == category_data_keys[-1]: continue
		a = []
		a.append(data_cell(str(N_of_item), widh_of_column[0]))
		a.append(data_cell(item, widh_of_column[1]))
		for j in range(len(data_base[item])):
			a.append(data_cell(data_base[item][j], widh_of_column[j+2]))
		print(*a, sep = '')

		N_of_item += 1

	return None


def represent_catalog(category_data_keys,cart):
	"""take nothing, return filtered or sorted list of names, 'back' or 'go to cart' """
	#returns choosen action from list of action
	while True:
		clear()
		catalog_logo()
		represent_table(category_data_keys)
		print('\n[0] [< back]  |  Functions : [1] filter, [2] sort, [3] add to cart, [4] go to cart')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(5):
			if response == '0': return 'back'

			######## filter
			elif response == '1':
				filtered_keys = represent_filter_attributes(category_data_keys)
				if filtered_keys != 'back':
					return filtered_keys
			######## filter

			######## sorter
			elif response == '2':
				sorted_keys = represent_sort_attributes(category_data_keys)
				if sorted_keys != 'back':
					return sorted_keys
			####### sorter

			####### add to cart
			elif response == '3':
				add_to_cart(category_data_keys,cart)
			####### add to cart

			####### go to cart
			elif response == '4': return 'go to cart'
			####### go to cart
		else:
			bad_input()
#######################################################################  catalog


#######################################################################  catalog filter
def represent_filter_attributes(category_data_keys):
	"""take list of names, return filtered list of names or 'back' """
	data_base = data_from_keys(category_data_keys)
	while True:
		clear()
		print('[0] [< back]\n============\nFilter by: \n[1]    default')
		n = 2
		for attribute in data_base[category_data_keys[-1]][1:-1]:
			print('[' + str(n) + '] ' + (' ' * (4 - len(str(n)))) + attribute)
			n += 1
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(n):
			if response == '0': return 'back'
			elif response == '1': return [] #### default

			else:
				attribute = data_base[category_data_keys[-1]][int(response)-1]
				attribute_value =  represent_filter_attributes_values(category_data_keys,attribute)
				if attribute_value == 'back': continue
				else:
					return attribute_value
		else:
			bad_input()


def represent_filter_attributes_values(category_data_keys,attribute):
	"""take list of names and name of attribute, return sorted list of names or 'back' """
	data_base = data_from_keys(category_data_keys)
	while True:
		clear()
		print('[0] [< back]\n============\nChoose value:')
		index_of_attribute = data_base[category_data_keys[-1]].index(attribute)
		set_of_values = []
		n = 1
		for item in category_data_keys:
			if item == category_data_keys[-1]: continue
			set_of_values.append(data_base[item][index_of_attribute])

		if  attribute in ['price', 'quantity in stock']:
			set_of_values = sorted(list(set(set_of_values)),key = float)
		else:
			set_of_values = sorted(list(set(set_of_values)))

		for i in set_of_values:
			print('[' + str(n) + ']' + (' ' * (5 - len(str(n)))) + str(i))
			n += 1
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(n):
			if response == '0':
				return 'back'
			else:
				return filter_by_attribute_value(category_data_keys, set_of_values[int(response)-1])
		else:
			bad_input()


def filter_by_attribute_value(category_data_keys, value_of_attribute):
	"""take list of names and value of attribute, return sorted list of names"""
	data_base = data_from_keys(category_data_keys)
	filtered_data_keys = [category_data_keys[-1]]
	for item in data_base:
		if value_of_attribute in data_base[item]:
			filtered_data_keys.append(item)
	return sorted(filtered_data_keys)
#######################################################################  catalog filter





#######################################################################  catalog sorter
def represent_sort_attributes(category_data_keys):
	"""take nothing, return 'back', return sort sorted list of names or 'back' """
	while True:
		clear()
		print('[0] [< back]\n============\nSort by: \n[1] default, \n[2] price \n[3] quantity in stock')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(4):
			if response == '0': return 'back'
			elif response == '1': return category_data_keys  #### default
			elif response == '2':
				sorted_keys_by_price =  represent_sort_attributes_values(category_data_keys,'price')
				if sorted_keys_by_price != 'back':
					return sorted_keys_by_price
			elif response == '3':
				sorted_keys_by_quantity = represent_sort_attributes_values(category_data_keys, 'quantity in stock')
				if sorted_keys_by_quantity != 'back':
						return sorted_keys_by_quantity
		else:
			bad_input()


def represent_sort_attributes_values(category_data_keys, attribute):
	"""take list of names and name of attribute, return return sorted list of names or 'back' """
	while True:
		clear()
		print('[0] [< back]\n============\nSort ' + attribute +  ': \n[1] ascending \n[2] descending')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(3):
			if response == '0': return 'back'
			elif response == '1': return sort_by_attribute_value(category_data_keys, attribute + ':ascending')
			elif response == '2': return sort_by_attribute_value(category_data_keys,attribute + ':descending')
		else:
			bad_input()


def sort_by_attribute_value(category_data_keys, attribute_value):
	"""take list of names and value of attribute, return sorted list of names """
	head = category_data_keys[-1]
	data_base = data_from_keys(category_data_keys)
	atribute_index = data_base[head].index(attribute_value.split(':')[0])
	if attribute_value.split(':')[1] == 'ascending':
		category_data_keys = sorted(category_data_keys[:-1], key = lambda x: float(data_base[x][atribute_index]))
		category_data_keys.append(head)
	elif attribute_value.split(':')[1] == 'descending':
		category_data_keys = sorted(category_data_keys[:-1], key = lambda x: float(data_base[x][atribute_index]), reverse = True)
		category_data_keys.append(head)
	return category_data_keys

#######################################################################  catalog sorter


#######################################################################  add to cart
def add_to_cart(category_data_keys,cart):
	"""take list of names and cart value, return cart value with added items """
	while True:
		clear()
		catalog_logo()
		represent_table(category_data_keys)
		print('\n[0] [<back]   |   Input # of item: ')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(len(category_data_keys)):
			if response == '0': return cart
			item = category_data_keys[int(response)-1]
			item_qantity = set_quantity(item)
			if item_qantity == 'back': continue
			cart.append([item,item_qantity])
			clear()
			print(f'You added {item_qantity} pieces of {item} to yout cart')
			input('\nPressc ENTER to continue')
		else:
			bad_input()


def set_quantity(item):
	"""take item name, return input quantity of items """
	clear()
	max_item_quatity = item_values(item)[-2]
	while True:
		print(f'[0] [<back]   |   Input quantity (available from 1 to {max_item_quatity}): ')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(int(max_item_quatity)+1):
			if response == '0': return 'back'
			return response
		else:
			bad_input()


def item_values(item):
	"""take item name, return its value from data """
	for dict in data.db:
		if item in dict:
			return dict[item]
#######################################################################  add to cart


####################################################################### cart
def represent_cart(cart):
	"""take cart value, return sorted cart value and display cart values """
	clear()
	cart_logo()
	item = ''
	sorted_cart = []
	for i in cart: # unite items from the same name and set availble quanity
		if i[0] != item:
			item = i[0]
			filtered_by_item = list(filter(lambda x: x[0] == item, cart))
			item_qantity = 0
			for j in filtered_by_item:
				item_qantity += int(j[1])
			sorted_cart.append([item,min(item_qantity,int(item_values(item)[-2]))])
	cart = sorted_cart

	max_len = 40 # dinamic width of name column
	for i in cart:
		if len(i[0]) > max_len:
			max_len = len(i[0])
	n = 1
	head = ['__#__|', f'_name{"_" * (max_len - 4)}_|', '_quantity_|','_price_for_one____|', '_price____________|']

	table_legth = 0
	for i in head:
		table_legth += len(i)
	while True:
		print('_' * (table_legth - 1))
		print(*head, sep = '')
		total_price = 0
		for i in cart:
			item_price = item_values(i[0])[-3]
			total_price += round(Decimal(item_price) * i[1],2)
			print(	' ' + str(n) + ' ' * (4 - (len(str(n)))) + '|',
					' ' + str(i[0]) + ' ' * (max_len - len(str(i[0]))) + ' |',
					' ' + str(i[1]) + ' ' * (9 - len(str(i[1]))) +'|',
					' ' + str(item_price) + ' ' * (len(head[-2]) - 2 - len(item_price)) + '|',
					' ' + str(round(Decimal(item_price) * i[1],2)) + ' ' * (len(head[-1]) - 2 - len( str(round(Decimal(item_price) * i[1],2)))) + '|', sep = '')
			n += 1
		print(f'\nTotal price: {total_price}')

		return cart


def represent_cart_func(cart):
	"""take cart value, return taken cart value, edited cart value, 'back' or 'exit' """
	while True:
		print('\n[0] [< back]  |  Functions : [1] edit , [2] info, [3] buy')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(4):
			if response == '0': return 'back'
			elif response == '1':
				edit = edit_func(cart)
				if edit != 'back': return edit
			elif response == '2':
				info_func(cart)
			elif response == '3':
				buy = buy_func(cart)
				if buy == 'exit': return 'exit'
			return cart
		else:
			bad_input()
			return cart
####################################################################### cart

####################################################################### cart edit
def edit_func(cart):
	"""take cart value, return edited cart value or 'back' """
	while True:
		clear()
		print('[0] [< back]\n============\nEdit: \n[1] items quantity \n[2] cart')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(3):
			if response == '0': return 'back'
			elif response == '1':
				edited_quantity = edit_quantity(cart)
				if edited_quantity != 'back': return edited_quantity
			elif response == '2':
				edited_cart = edit_cart(cart)
				if edited_cart != 'back': return edited_cart
			continue
		else:
			bad_input()


def edit_quantity(cart):
	"""take cart value, return edited by changing of quantity cart value or 'back' """
	while True:
		clear()
		cart = represent_cart(cart)
		print('\n[0] [<back]   |   Input # of the item whose quantity is need to change: ')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(len(cart)+1):
			if response == '0': return 'back'
			new_quantity =  set_quantity(cart[int(response)-1][0])
			if new_quantity == 'back': continue
			cart[int(response)-1][1] = new_quantity
			return cart
		else:
			bad_input()


def edit_cart(cart):
	"""take cart value, return edited by deleting cart value or 'back' """
	while True:
		clear()
		cart = represent_cart(cart)
		print('\n[0] [<back]   |   Input # of the item whose need to delete: ')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(len(cart)+1):
			if response == '0': return 'back'
			for index in range(len(cart)):
				if int(response) - 1 == index:
					del cart[index]
					return cart
		else:
			bad_input()
####################################################################### cart edit

####################################################################### cart info
def info_func(cart):
	"""take cart value, display item detailed info or return 'back' """
	while True:
		clear()
		cart_logo()
		cart = represent_cart(cart)
		print('\n[0] [<back]   |   Input # of the item whose information is need to display: ')
		response = input('\n>>> ')
		if response.isdecimal() and int(response) in range(len(cart)+1):
			if response == '0': return 'back'
			item = cart[int(response)-1][0]
			category_data_keys = [item,'name:']
			clear()
			represent_table(category_data_keys)
			input('\nPress ENTER to back')
		else:
			bad_input()
####################################################################### cart info


####################################################################### cart buying
def buy_func(cart):
	""""take cart value, return 'exit' or taken cart value"""
	while True:
		clear()
		represent_cart(cart)
		print('\n[0] [<back]\nInput your phone number: ')
		response = input('\n>>> ')
		if response.isdecimal() and len(response) > 1:
			phone = response
			while True:
				clear()
				represent_cart(cart)
				print('\nInput your name: ')
				response = input('\n>>> ')
				name = response
				if response.isalpha():
					N_order = order_generator()
					clear()
					print(	f"Your order No: {N_order}.",
							"Our specialist will contact you to confirm your order.",
							"For all questions contact the number 8-800-555-35-35/", sep = '\n')
					data.db_oders.update({N_order:[cart,name,phone]})
					input('\nPress ENTER to exit')
					return 'exit'
				else:
					bad_input()
		elif response.isdecimal() and response == '0':
			return cart
		else:
			bad_input()
####################################################################### cart buying



####################################################################### tech stuff
def order_generator():
	""""take nothing, return 6 digits value"""
	while True:
		order = ''
		for i in range(6):
			order += str(randint(0,9))
		if order in data.db_oders:
			continue
		else:
			return order

def clear():
	""""take nothing, clear console"""
	system('cls||clr')


def bad_input():
	"""take noting, diplay warning, clear console"""
	clear()
	print('>>> bad input <<<')
	sleep(1)
	clear()
	return None



def go_to_cart(cart):
	while True:
		sorted_cart = represent_cart(cart)
		edited_cart = represent_cart_func(sorted_cart)
		if edited_cart == 'back': return sorted_cart
		elif edited_cart == 'exit': return 'exit'
		else: cart = edited_cart


def catalog_logo():
    	print(	r' _________________________________________________',
				'|   _      ___           __   __  | |_1_|_____|_| |',
				'|  |   /\   |   /\  |   |  | | _  | |_2_|_____|_| |',
				'|  |_ /--\  |  /--\ |__ |__| |__| | |_3_|_____|_| |',
				'|_________________________________|_|_4_|_____|_|_|', sep = '\n')

def cart_logo():
	print( r' _________________________________________________',
			'|         _       __   ___        |   /\#####/    |',
			'|        |   /\  |__|   |         |     \###/     |',
			'|        |_ /--\ |  \   |         |    __\____    |',
			'|_________________________________|____O_____O____|', sep = '\n')



def data_from_keys(category_data_keys):
	"""take list of names (names of items in data base), return data from categogy of items"""
	data_base = {}
	for dict in data.db: ## ok
		if category_data_keys[0] in dict:
			for item in category_data_keys:
				data_base.update({item:dict[item]})
	return data_base
####################################################################### tech stuff

