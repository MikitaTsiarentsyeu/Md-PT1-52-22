import bl

def show_all_categories():
    print(f'Product categories:\n{bl.get_all_categories()}')

def choose_category(category):
    if bl.choose_category(category):
       print(f'{category}:')
       print(bl.choose_category(category))
    else:
        print("No such category. Try again\n")

def show_products_in_cart():
    print(f'Your cart: \n{bl.get_cart()}\nTotal to pay: {bl.total_price()} USD\n')

def add_product(code, amount):
    print(bl.add_product(code, amount))

def confirm_the_order():
    print (f'Total to pay: {bl.total_price()} USD \nThank you for the order\n')
    bl.clean_cart()

def cancel_order():
    bl.clean_cart()

def start_main_flow():
    while True:
        chosen = input("""Enter the number of your operation:
        0. Exit
        1. Show all categories of products
        2. Choose the category
        3. Add product to the cart
        4. Show your cart
        5. Confirm your order
        6. Cancel order
        """)

        if chosen == '0':
            break
        elif chosen == '1':
            show_all_categories()
        elif chosen == '2':
            c = input("Enter the category of products: ")
            if c == '2':
                c = "vegs"
            elif c == '1':
                c = 'fruits'
            choose_category(c)
        elif chosen == '3':
            b = input("Enter product code: ")
            c = input("Enter amount: ")
            add_product(b, c)
        elif chosen == '4':
           show_products_in_cart()
        elif chosen == '5':
           confirm_the_order()
        elif chosen == '6':
           cancel_order()
           show_products_in_cart()
        else:
           print ('Invalid number of operation\n')
        continue
