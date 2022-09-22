import data

def get_position(number):
    if number == 0:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        all_product = {**fender, **gibson, **ibanez, **jackson, **yamaha, **gretsch}
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in all_product.items()])
    elif number == 1:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in fender.items()])
    elif number == 2:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in gibson.items()])
    elif number == 3:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in ibanez.items()])
    elif number == 4:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in jackson.items()])
    elif number == 5:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in yamaha.items()])
    elif number == 6:
        fender, gibson, ibanez, jackson, yamaha, gretsch = data.get_position()
        return '\n'.join([f"(Code of product {c}),{n[0]}, Name - {n[1]}, Price - {n[2]}$, Stock availability - {n[3]}" for c,n in gretsch.items()])


def add_in_cart(p_number):
    if 1000 < p_number < 2000 and data.data_shop_fender.get(p_number):
        data.add_in_cart(p_number,data.data_shop_fender)
        return f"Product has been added to cart"
    elif 2000 < p_number < 3000 and data.data_shop_gibson.get(p_number):
        data.add_in_cart(p_number,data.data_shop_gibson)
        return f"Product has been added to cart"
    elif 3000 < p_number < 4000 and data.data_shop_ibanez.get(p_number):
        data.add_in_cart(p_number,data.data_shop_ibanez)
        return f"Product has been added to cart"
    elif 4000 < p_number < 5000 and data.data_shop_jackson.get(p_number):
        data.add_in_cart(p_number,data.data_shop_jackson)
        return f"Product has been added to cart"
    elif 5000 < p_number < 6000 and data.data_shop_yamaha.get(p_number):
        data.add_in_cart(p_number,data.data_shop_yamaha)
        return f"Product has been added to cart"
    elif 6000 < p_number < 7000 and data.data_shop_gretsch.get(p_number):
        data.add_in_cart(p_number,data.data_shop_gretsch)
        return f"Product has been added to cart"
    else:
        return f"Product with this code is not in the catalog"

def get_shopping_cart():
    return '\n'.join([f"{n[0]} - {n[1]}, name - {n[2]}, price - {n[3]}$" for n in data.get_shopping_cart()])

def get_deposit():
    return data.get_deposit()

def set_deposit(number):
    data.set_deposit(number)

def get_price():
    return data.get_price()

def clean_cart():
    data.clean_cart()

def remove_product(number):
    data.remove_product(int(number))

def count_cart():
    return data.count_cart()