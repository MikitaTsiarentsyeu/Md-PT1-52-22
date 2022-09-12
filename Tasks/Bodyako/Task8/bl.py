import data 

def get_iphone():
    res = data.get_iphone()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_samsung():
    res = data.get_samsung()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_xiaomi():
    res = data.get_xiaomi()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def cart_iphone(code):
    res = data.cart_iphone(code)
    return res

def cart_samsung(code):
    res = data.cart_samsung(code)
    return res

def cart_xiaomi(code):
    res = data.cart_xiaomi(code)
    return res

def price_iphone(code):
    res = data.price_iphone(code)
    return res

def price_samsung(code):
    res = data.price_samsung(code)
    return res

def price_xiaomi(code):
    res = data.price_xiaomi(code)
    return res