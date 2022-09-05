import bl

def get_iphone():
    res = bl.get_iphone()
    print(res)

def get_samsung():
    res = bl.get_samsung()
    print(res)

def get_xiaomi():
    res = bl.get_xiaomi()
    print(res)

def cart_iphone():
    code = int(input('Choose the code of the product:\n'))
    res = bl.cart_iphone(code)
    res2 = bl.price_iphone(code)
    return cart_full(res, int(res2))

def cart_samsung():
    code = int(input('Choose the code of the product:\n'))
    res = bl.cart_samsung(code)
    res2 = bl.price_samsung(code)
    return cart_full(res, int(res2))

def cart_xiaomi():
    code = int(input('Choose the code of the product:\n'))
    res = bl.cart_xiaomi(code)
    res2 = bl.price_xiaomi(code)
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
        sum = sum (item)
        print (f'The total price is: {sum} USD')

        input ('Thank you!\nPress enter to continue')

def main_flow():
    while True:
        chosen = input('''Choose brand:
        1.iPhone
        2.Samsung
        3.Xiaomi
        ''')
        if chosen == '1':
            get_iphone()
            cart_iphone()
        elif chosen == '2':
            get_samsung()
            cart_samsung()
        elif chosen == '3':
            get_xiaomi()
            cart_xiaomi()
        else:
            break