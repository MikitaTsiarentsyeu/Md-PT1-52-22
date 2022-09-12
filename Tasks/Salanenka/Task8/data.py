stocks = [{'name': 'Iphone 13', 'category': 'Mobile phones', 'code': '11','price': 1000, 'stock': 10}, {'name': 'Samsung Galaxy', 'category': 'Mobile phones', 'code': '12', 'price': 800,'stock': 10}, {'name': 'Sony Bravia', 'category': 'TVs', 'code': '13', 'price': 1500,'stock': 10}, {'name': 'Dell g15', 'category': 'Computers', 'code': '14','price': 1200, 'stock': 10}, {'name': 'ASUS ZenBook','category': 'Computers', 'code': '15','price': 1300, 'stock': 20}, {'name': 'Samsung', 'category': 'TVs', 'code': '16', 'price': 1150,'stock': 15}]

categories2=[]
cart= []
def get_all_categories():
    categories= []
    for i in stocks:
        categories.append(i['category'])
    global categories2 
    categories2= (sorted(list(set(categories))))
    return categories2

def get_all_products ():
    return stocks

def all_products ():
    for i in stocks:
        print (i)

def find_product(code):
    for i in stocks:
        if i.get('code')==str(code):
            return stocks.index(i)

def find_price (product):
    i = stocks[product]
    return i.get('price')

def find_stock(product):
    i = stocks[product]
    return i.get('stock')

def change_stock(product,rest):
    stocks[product]['stock']= rest
    return True

def all_category_products(category):
    category_list=[]
    for i in stocks:
        if i['category']==category and i['stock']>0:
            category_list.append(i)
    return category_list

def add_order(product, amount, total_price):
    cart.append([stocks[product]['name'], amount, total_price])
    return cart

def show_cart():
    return cart

def clean_cart():
    global cart 
    cart = []