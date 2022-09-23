import data

def get_position(number):
    if number == 0:
        mob, note, watch = data.get_position()
        all_product = {**mob,**note,**watch}
        return '\n'.join([f"(Product code {c}),{n[0]}, name - {n[1]}, price - {n[2]}$, quantity of stock - {n[3]}" for c,n in all_product.items()])
    elif number == 1:
        mob, note, watch = data.get_position()
        return '\n'.join([f"(Product code {c}),{n[0]}, name - {n[1]}, price - {n[2]}$, quantity of stock - {n[3]}" for c,n in mob.items()])
    elif number == 2:
        mob, note, watch = data.get_position()
        return '\n'.join([f"(Product code {c}),{n[0]}, name - {n[1]}, price - {n[2]}$, quantity of stock - {n[3]}" for c,n in note.items()])
    elif number == 3:
        mob, note, watch = data.get_position()
        return '\n'.join([f"(Product code {c}),{n[0]}, name - {n[1]}, price - {n[2]}$, quantity of stock - {n[3]}" for c,n in watch.items()])

def add_in_cart(p_number):
    if 1000 < p_number < 2000 and data.shop_data_mobilefone.get(p_number):
        data.add_in_cart(p_number,data.shop_data_mobilefone)
        return f"Product has been added to cart"
    elif 2000 < p_number < 3000 and data.shop_data_notebook.get(p_number):
        data.add_in_cart(p_number,data.shop_data_notebook)
        return f"Product has been added to cart"
    elif 3000 < p_number and data.shop_data_watch.get(p_number):
        data.add_in_cart(p_number,data.shop_data_watch)
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





