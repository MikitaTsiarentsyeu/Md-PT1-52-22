brand = {1:'Apple', 2:'Samsung', 3:'Xiaomi'}

iphone = {11111:('iPhone 11 Pro Max 64GB', '975', 'USD'), 12222:('iPhone 12 Pro Max 128GB', '1488', 'USD'), 13333:('iPhone 13 Pro Max 128GB', '1328', 'USD')}

samsung = {21111:('Galaxy S21 256GB', '913', 'USD'), 22222:('Galaxy S20 Ultra 128GB', '1020', 'USD'), 23333:('Galaxy S22 128GB', '890', 'USD')}

xiaomi = {31111:('Redmi Note 11 Pro 128GB', '375', 'USD'), 32222:('Mi 11 Ultra 256GB', '940', 'USD'), 33333:('Redmi Note 11S 128GB', '300', 'USD')}

def get_brand():
    return brand.values()

def get_iphone():
    return iphone.items()

def get_samsung():
    return samsung.items()

def get_xiaomi():
    return xiaomi.items()

def cart_iphone(code):
    for c, n in iphone.items():
        if c == code:
           return n[0]

def cart_samsung(code):
    for c, n in samsung.items():
        if c == code:
           return n[0]

def cart_xiaomi(code):
    for c, n in xiaomi.items():
        if c == code:
           return n[0]

def price_iphone(code):
    for c, n in iphone.items():
        if c == code:
           return n[1]

def price_samsung(code):
    for c, n in samsung.items():
        if c == code:
           return n[1]

def price_xiaomi(code):
    for c, n in xiaomi.items():
        if c == code:
           return n[1]