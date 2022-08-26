import decimal


d = {"bread": "food, 556008, 5.53, 20", "potato": "food, 202004, 1.11, 100", "banana": "food, 954610, 2.93, 999",
     "hammer": "tools, 987690, 10.13, 5", "screwdriver": "tools, 820092, 7.10, 4", "T-shirt": "clothes, 031450, 30.04, 100"}

c = {}


wallet = decimal.Decimal(100.00)
summ = decimal.Decimal(0.00)


def get_all_categories():
    return ("\n".join(list(set([[i for i in d.values()][i].split(", ")
                               [0] for i in range(len([i for i in d.values()]))])))).strip('\n')


def get_goods_from_category(name):
    l = []
    for i in d:
        if d[i].find(name) != -1:
            l.append(i)
            s = ("".join([f"{i} = {d[i].split(', ')[3]} pcs left, {d[i].split(', ')[2]} $\n" for i in l])).strip('\n')
    return None if l == [] else s


def minus_in_cart(name, n):
    l = d[name].split(', ')[0:3]
    if int(d[name].split(', ')[3])-n >= 0:
        l.append(str(int(d[name].split(', ')[3])-n))
    else:
        return -1
    if name not in c:
        c[name] = n
    else:
        c[name] = str(int(c[name]) + n)
    d[name] = ", ".join(l)


def get_cart():
    return c


def get_serials():
    l = []
    for i in d:
        l.append(i)
        ser = ("".join([f"{i}: {d[i].split(', ')[1]}\n" for i in l])).strip('\n')
    return ser


def clear_cart_and_sum():
    global c
    global summ
    global wallet
    summ = 0.00
    c = {}
    return c


def balance_reducing():
	global wallet
	global summ
	wallet = wallet - summ


def wallet_balance():
    global wallet
    return wallet


def full_sum(name, n):
    global summ
    summ += decimal.Decimal(d[name].split(", ")[2]) * n


def total_payment():
    global summ
    return summ
    

def prod_price(name):
	return decimal.Decimal(d[name].split(", ")[2])