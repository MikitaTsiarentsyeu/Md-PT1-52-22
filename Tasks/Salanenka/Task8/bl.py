import data

def get_all_products ():
    stocks1 = data.get_all_products()
    stocks2 = []
    for i in stocks1:
        stocks2.append (f"{i['name']}, сategory: {i['category']}, code: {i['code']}, price: {i['price']}")
    return '\n'.join(stocks2)

def get_all_categories():
    list1 = data.get_all_categories()
    list2 = list(map(lambda i:f'{list1.index(i)+1}.{i}',list1))
    return '\n'.join(list2)

def category_chosen(category_number):
    category = data.categories2[int(category_number)-1]
    return category

def all_category_products(category):
    category_list = data.all_category_products(category)
    list1=[]
    for i in category_list:
        list1.append(f"{i['name']}, code: {i['code']}, price: {i['price']}")
    return '\n'.join(list1)

def total_price(product, amount):
    price = data.find_price(product)
    return amount*price

def change_stock(product,amount):
    rest = data.stocks[product]['stock']-amount
    return data.change_stock(product,rest)

def add_order(product, amount):
    if validate_stock(product,amount):
        tot_price = total_price(product,amount)
        data.add_order(product, amount, tot_price)
        change_stock(product, amount)
        return (f'You added {data.stocks[product]["name"]}, {amount} pcs., total: {tot_price} USD')
    if not validate_stock (product, amount):
        return (f'Sorry, we have only {data.find_stock(product)} pcs. in stock')

def validate_product (code):
    return data.find_product(code)

def validate_stock(code, amount):
    if data.find_stock(code)>= amount:
        return True
    return False

def show_cart():
    cart=[]
    for i in data.show_cart():
        cart.append(f'{i[0]}, {i[1]} pcs.,: {i[2]} USD')
    if cart == []:
        return 'Empty'
    return '\n'.join(cart)

def calculate_cart():
    total = 0
    for i in data.cart:
        total+=i[2]
    return total

def clean_cart():
    data.clean_cart()

