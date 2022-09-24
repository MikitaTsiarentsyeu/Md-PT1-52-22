product = {1:'Socks', 2:'Skirt', 3:'Sneakers'}

socks = {11:('Pink unicorn', '9', 'USD'), 21:('Avocado-singer', '13', 'USD'), 31:('Girl in a hood', '11', 'USD')}

skirt = {12:('Red and bold', '90', 'USD'), 22:('Serios monday', '100', 'USD'),32:('Light cocktail', '120', 'USD')}

sneakers = {13:('From dirt to Kings', '150', 'USD'), 23:('Bright fly', '120', 'USD'), 33:('Ghost', '250', 'USD')}

def get_product():
    return product.values()

def get_socks():
    return socks.items()

def get_skirt():
    return skirt.items()

def get_sneakers():
    return sneakers.items()

def cart_socks(code):
    for c, n in socks.items():
        if c == code:
           return n[0]

def cart_skirt(code):
    for c, n in skirt.items():
        if c == code:
           return n[0]

def cart_sneakers(code):
    for c, n in sneakers.items():
        if c == code:
           return n[0]

def price_socks(code):
    for c, n in socks.items():
        if c == code:
           return n[1]

def price_skirt(code):
    for c, n in skirt.items():
        if c == code:
           return n[1]

def price_sneakers(code):
    for c, n in sneakers.items():
        if c == code:
           return n[1]