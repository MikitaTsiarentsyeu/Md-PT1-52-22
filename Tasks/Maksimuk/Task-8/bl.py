import data 

def get_socks():
    res = data.get_socks()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_skirt():
    res = data.get_skirt()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_sneakers():
    res = data.get_sneakers()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def cart_socks(code):
    res = data.cart_socks(code)
    return res

def cart_skirt(code):
    res = data.cart_skirt(code)
    return res

def cart_sneakers(code):
    res = data.cart_sneakers(code)
    return res

def price_socks(code):
    res = data.price_socks(code)
    return res

def price_skirt(code):
    res = data.price_skirt(code)
    return res

def price_sneakers(code):
    res = data.price_sneakers(code)
    return res