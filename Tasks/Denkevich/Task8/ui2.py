import bl2

def show_balance():
	return print(bl2.get_current_balance())

def show_total():
	return print(bl2.get_total())

def show_everything():
	print()
	show_balance()
	show_total()

def addit_exit():
	print("  0. Back to menu")

def exit():
	return print("\n- Thank you, come again.\n")

def incorrect_1():
	return print("INCORRECT INPUT", end="")
	
def incorrect_2():
	return print("\nINCORRECT INPUT", end="")

def choice_validation(func):
	def wrap(choice):
		while True:
			f = func(choice)
			if f == -1:
				choice = input(f"\nINCORRECT INPUT. TRY AGAIN:\n")
				continue
			if f == -2:
				return -1
			else:
				return print(f"{f}")
	return wrap

def show_assort():
	return print(bl2.edit_assort())

def show_categories():
	return print(bl2.edit_categories())

@choice_validation
def choose_category(choice):
	return bl2.edit_list(choice)

@choice_validation
def choose_product(choice):
		return bl2.edit_prod(choice)

def add_to_cart_choice(choice):
	if bl2.check_count()==False:
		return print("- Store dosn't contain this product anymore.")
	while True:
		if choice == "1":
			return print(bl2.add_to_cart(), end = "")
		elif choice == "2":
			return
		else:
			choice = input(f"\nINCORRECT INPUT. TRY AGAIN:\n")
			continue

def show_cart():
	c = bl2.edit_cart()
	if c == "":
		return print("\nEmty")
	else:
		print(f"\n{c}\n  0. Back\n  1. Choose the product to remove")
		choice= input()
		if choice == "0":
			return
		elif choice == "1":
			print("\n- What product do you want to remove?")
			print(f"  {bl2.list_order()}")
			choice = input()
			return print(bl2.remove_product(choice), end="")
		else:
			return print(f"\nINCORRECT INPUT.", end="")

def make_order_if_cart():
	c = bl2.edit_cart()
	if c == "":
		return print("- Your cart is empty. Add something.", end="")
	else:
		choice = input("\n- Are you ready to pay for it?\n  1. Yes\n  2. No\n")
		make_order(choice)
		

def make_order(choice):
	if choice == "1":
		return print(bl2.make_order())
	elif choice == "2":
		return
	else:
		return print(f"\nINCORRECT INPUT.")

def user_int():
	while True:
		show_everything()
		n = input("""  0. Exit
  1. Buy something
  2. Check a cart
  3. Pay the order
""")
		if n == "0":
			exit()
			break
		elif n == "1":
			show_categories()
			choice = input()
			if choose_category(choice) == -1:
				continue
			choice = input()
			if choose_product(choice) == -1:
				continue
			choice = input()
			add_to_cart_choice(choice)
		elif n == "2":
			show_cart()
		elif n == "3":
			make_order_if_cart()
		elif n == "":
			incorrect_1()
		else:
			incorrect_2()