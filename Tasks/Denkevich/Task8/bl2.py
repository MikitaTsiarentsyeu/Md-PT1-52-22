import data2

def get_current_balance():
	w = data2.get_balance()
	return f"Current balance: {w} $"

def get_total():
	t = data2.get_total()
	return f"Total order cost: {t} $"
	
def edit_assort():
	res = ""
	l1 = data2.get_assort()
	l2 = data2.get_prices()
	for i in range(len(l1)):
		res += f"{l1[i]} - {l2[i]} $\n"
	return res
	
def edit_categories():
	s = []
	[s.append(i) for i in data2.get_categories() if i not in s]
	l = []
	for i in range(len(s)):
		l.append(f"{i+1}. {s[i].capitalize()}")
	res = "\n  ".join(l)
	return f"\n- Our store contains the folowing categories:\n  {res}\n  (0. Back to menu)\n\n- Please enter category number:"

def edit_list(choice):
	try:
		if choice == "0":
			return -2
		s = data2.get_assort(choice)[0]
		p = data2.get_assort(choice)[1]
	except:
		return -1
	l = []
	for i in range(len(s)):
		l.append(f"{i+1}. {s[i].capitalize()} - {p[i]} $")
	res = "\n  ".join(l)
	return f"  {res}\n  (0. Back to menu)\n\n- Choose a product:"
	
def edit_prod(choice):
	if choice == "0":
		return -2
	b = data2.get_prod(choice)
	if b == False:
		return -1
	c = data2.get_count(choice)
	return f"\n- Add {b} to cart? {c} pcs left.\n  1. Yes\n  2. No"

def add_to_cart():
	data2.count_refresh()
	data2.cart_refresh()
	data2.total_refresh()
	return f"- Done. Check your cart.\n"
	
	# if data2.get_total() > data2.get_balance():
	# 	return f"You're haven't enough money to pay for it."
	
def edit_cart():
	c = ", ".join(data2.get_cart())
	return f"{c}"
	
def make_order():
	if data2.get_total() > data2.get_balance():
		return f"- You're haven't enough money to pay for it."
	else:
		data2.refresh_cart_and_balance()
		return f"- Payment was succssesfull"
		
def list_order():
	c = data2.get_cart()
	l = [f"{i+1}. {c[i]}" for i in range(len(c))]
	return "\n  ".join(l)

def remove_product(choice):
	try:
		c = data2.get_cart()
		data2.return_total(c[int(choice)-1])
		del c[int(choice)-1]
		return f"- Product was removed from a cart\n"
	except:
		return f"\nINCORRECT INPUT"

def check_count():
	if data2.count() == 0:
		return False