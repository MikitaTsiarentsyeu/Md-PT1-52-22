import data


def get_all_categories():
    return data.get_all_categories()


def get_goods_from_category(name):
    return data.get_goods_from_category(name)


def minus_in_cart(name, n):
    return data.minus_in_cart(name, n)
    
    
def get_cart():
	k = data.get_cart()
	if k == {}:
		return -1
	else:
		s = "; ".join([f"{i}, {k[i]} pcs" for i in k])
		return s


def compact_serials():
    return data.get_serials()
    

def prepare_cart_and_sum():
    return data.clear_cart_and_sum()


def full_sum(name, n):
    return data.full_sum(name, n)


def wallet_balance():
    return f"{data.wallet_balance()} $"


def total_payment():
    return data.total_payment()
    
   
def balance_reducing():
	data.balance_reducing()
	
def if_sum_exeeding(name, n):
	c = data.prod_price(name)
	w = data.wallet_balance()
	s = data.total_payment()
	d = w - s - (c * n)
	if d < 0:
		return -1