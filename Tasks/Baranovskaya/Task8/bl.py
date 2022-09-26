import data
from decimal import Decimal

def get_all_categories():
    categories = data.get_all_categories()
    return '\n'.join([f"{c}" for c in categories.keys()])

def choose_category(category):
    products = data.choose_category(category)
    if products == None:
        return False
    return '\n'.join([f"{p[0]} - code: {p[1]}, price: {p[2]}$, amount: {p[3]} pcs." for p in products])

def add_product(code, amount):
    if data.add_product(code, amount):
       return 'Product added to your shopping cart.\n'
    return 'Check your input and try again.\n'

def get_cart():
    cart=[]
    for i in data.get_cart():
        cart.append(f'{i[0]} - {i[1]} $, {i[2]} pcs.')
    if cart == []:
        return 'Empty'
    return '\n'.join(cart)

def clean_cart():
    data.clean_cart()

def total_price():
    cart = data.get_cart()
    total = 0
    for i in cart:
        total+=(Decimal(i[1])*Decimal(i[2]))
    return total