import bl

def get_socks():
    res = bl.get_socks()
    print(res)

def get_skirt():
    res = bl.get_skirt()
    print(res)

def get_sneakers():
    res = bl.get_sneakers()
    print(res)

def cart_socks():
    code = int(input('Choose the code one product:\n'))
    res = bl.cart_socks(code)
    res2 = bl.price_socks(code)
    return cart_full(res, int(res2))

def cart_skirt():
    code = int(input('Choose the code one product:\n'))
    res = bl.cart_skirt(code)
    res2 = bl.price_skirt(code)
    return cart_full(res, int(res2))

def cart_sneakers():
    code = int(input('Choose the code one product:\n'))
    res = bl.cart_sneakers(code)
    res2 = bl.price_sneakers(code)
    return cart_full (res, int(res2))

cart = []
item = []
def cart_full(res, res2):
    cart.append(res)
    item.append(res2)
    print(f"Your choice is:\n{', '.join(map(str,cart))}")
    res = input('Type 1 to continue purchase or 2 to get the final bill:\n')
    if res == '2':
        bill = (', '.join(map(str,cart)))
        print (f'Your order is:\n{bill}')
        fsum = sum (item)
        print (f'A good choice! The total price is: {fsum} USD')

        input ('Thanks a lot!\nPress enter to continue')

def main_flow():
    while True:
        chosen = input('''Choose type of product:
        1.Socks
        2.Skirt
        3.Sneakers
        ''')
        if chosen == '1':
            get_socks()
            cart_socks()
        elif chosen == '2':
            get_skirt()
            cart_skirt()
        elif chosen == '3':
            get_sneakers()
            cart_sneakers()
        else:
            break