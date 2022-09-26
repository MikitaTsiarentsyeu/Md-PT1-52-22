catalog = {
    "fruits": [['pineapples', '11', '2.75', '10'], ['apples', '12', '1.31', '30'], ['mango', '13', '1.81', '15']],
    "vegs": [['carrots', '21', '0.5', '40'], ['cucumbers', '22', '1.41', '25'], ['tomatoes', '23', '1.9', '31']]
}

cart = []

def get_all_categories():
    return catalog

def choose_category(category):
    return catalog.get(category)

def add_product(code, amount): 
    if code[0] == '1':
       products = catalog.get("fruits")
    elif code[0] == '2':
       products = catalog.get("vegs")
    else:
        return False
    for i in products:
        if i[1] == code:
            if int(amount)>int(i[3]) or amount=='0':
                return False
            else:
                i[3] = str(int(i[3]) - int(amount))
                cart.append([i[0], i[2], amount])
    return True

def get_cart():
    return cart

def clean_cart():
    global cart
    cart = []
