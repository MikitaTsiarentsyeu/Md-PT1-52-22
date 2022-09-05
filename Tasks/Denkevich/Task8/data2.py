from decimal import Decimal

d = {"bread": ["food", "56567890", "4.88", "20"], "potato": ["food", "202004", "1.11", "100"], "banana": ["food", "954610", "2.93", "999"],
     "hammer": ["tools", "987690", "10.13", "5"], "pliers": ["tools", "820092", "7.10", "4"],
     "t-shirt": ["clothes", "031450", "30.04", "100"], "pants": ["clothes", "021651", "35.10", "50"], "saw": ["tools", "523611", "19.02", "3"]}

cart = []

wallet = Decimal("100.00")
total = Decimal("0.00")

def get_categories():
	l = []
	for i in d.values():
		l.append(i[0])
	return l

def get_total():
	return total

def get_balance():
    return wallet

n = ""
def get_assort(choice):
	if int(choice) <= 0:
		return False
	l_assort = []
	l_price = []
	t = []
	global n
	n = choice
	[t.append(i) for i in get_categories() if i not in t]
	try:
		for i, v in d.items():
			if t[int(choice)-1] == v[0]:
				l_assort.append(i)
			if t[int(choice)-1] == v[0]:
				l_price.append(v[2])
		return l_assort, l_price
	except:
		return False

def get_prices():
    l = []
    for i in d.values():
        l.append(i[2])
    return l

n_prod = ""
def get_prod(choice):
	try:
		if int(choice) <= 0:
			return False
	except:
		return False
	global n_prod
	n_prod = choice
	try:
		s = get_assort(n)[0]
		el = s[int(choice)-1]
		return el
	except:
		return False


def get_count(choice):
	s = get_assort(n)[0][int(choice)-1]
	c = d[s][3]
	return c

def get_cart():
	return cart

def cart_refresh():
	global cart
	cart.append(get_prod(n_prod))
	return cart

def count_refresh():
	global d
	d[get_prod(n_prod)][3] = int(d[get_prod(n_prod)][3]) - 1

def total_refresh():
	global total
	total += Decimal(d[get_prod(n_prod)][2])
	
def refresh_cart_and_balance():
	global cart
	cart = []
	global wallet
	global total
	wallet = wallet - total
	total = Decimal("0.00")
	
def return_total(p): # correct it
	global total
	total -= Decimal(d[p][2])
	s = get_assort(n)[0]
	d[s[int(n_prod)-1]][3] = str(int(d[s[int(n_prod)-1]][3])+1)
	
	
def count():
	s = get_assort(n)[0]
	el = d[s[int(n_prod)-1]][3]
	return int(el)