import decimal
import data


def get_all_products():
    products = data.get_all_products()
    data_products = list()
    for i in products.keys():
        data_products.append(f"\nCategory:\n    -> {i}\nProducts:")
        for e in products[i].keys():
            data_products.append(
                f"    -> {e}: {products[i][e][1]} USD; {products[i][e][-1]} - amount; {products[i][e][0]} - product code.")
    return '\n'.join(data_products)


def get_all_categories():
    categories = data.get_all_categories()
    return '\n'.join([f"-> {name_category}" for name_category in categories])


def get_products(user_choice):
    products = data.get_products()
    if user_choice in products:
        data_category = products.get(user_choice)
        data_products = list()
        for i in data_category:
            data_products.append(
                f"{i}:\n    {data_category[i][1]} USD;\n    {data_category[i][-1]} - amount;\n    {data_category[i][0]} - product code.\n")
    return '\n'.join(data_products)


def get_add_products(add_prod):
    if add_prod:
        f = input("\nEnter product name: ")
        name_prod = data.get_add_products(f)
        cart = data.cart
        amount = get_buy_product()
        if name_prod == True:
            data_product = list()
            for i in cart:
                data_product.append(f"-> {i}: {cart[i][1]} USD;")
                data_cart = '\n'.join(data_product)
            return f"\nContents of your shopping cart:\n{data_cart}\n{amount}"
        else:
            return f"You entered incorrect data, please try again!"
    else:
        return f"You entered incorrect data, please try again!"


def get_buy_product():
    cart = data.cart
    amount_of_money = 0
    if cart:
        for i in cart:
            amount_of_money += decimal.Decimal(cart[i][1])
        return f"\nThe cost of your purchase: {amount_of_money} USD."
    else:
        return f"Cart is empty. Your check is {amount_of_money} USD."
