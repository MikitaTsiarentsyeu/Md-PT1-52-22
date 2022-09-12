import bl

def input_code():
    return input('Please input the code of product:\n')

def input_amount():
    return int(input('Please input the number of products you want to order:\n'))

def show_all_products():
    print(f'All our products:\n{bl.get_all_products()}')
    if_order()

def another_order(): 
    order = input("""\n Want to add some other products?
        0. No, finish shopping
        1. Yes, show all products 
        2. Yes, choose category
        3. Exit \n
        """)
    if order == '0':
        show_cart()
    elif order == '1':
        show_all_products()
    elif order == '2':
        choose_category()
    elif order == '3':
        return
    else:
        print ('Invalid number')
        another_order()

def new_order():
    while True:
        product = bl.validate_product(input_code())
        if product == None:
            print ('Invalid product code')
        else:
            break
    print(bl.add_order(product, input_amount()))
    another_order()

def choose_category():
    chosen = input (f'Choose the category:\n{bl.get_all_categories()}\n')
    chosen2 = bl.category_chosen(chosen)
    print(f'Products in category {chosen2}:\n{bl.all_category_products(chosen2)}')
    if_order()

def show_cart():
    print(f'Your cart: \n {bl.show_cart()}')
    pay=bl.calculate_cart()
    if pay == 0:
        return
    print(f'Total to pay: {bl.calculate_cart()} USD \n')
    confirm_order()

def confirm_order():
    confirm = input("""\n Want to confirm the order?
        0. No, exit
        1. Yes
        """)
    if confirm == '0':
        return
    elif confirm == '1':
        print (f'You can pick up your order in 2 days. Total to pay: {bl.calculate_cart()} USD \n Thank you for the order\n')
        bl.clean_cart()
    else:
        print ('Invalid number of operation')
        confirm_order()

def if_order(): 
    order = input("""\n Want to order any products?
        0. No, exit without shopping
        1. Yes
        2. Show my cart
        """)
    if order == '0':
        return
    elif order == '1':
        new_order()
    elif order == '2':
        show_cart()
    else:
        print ('Invalid number of operation')
        if_order()
        
def start_main_flow():
    while True:
        chosen = input("""Enter the number of your operation:
        0.Exit without shopping
        1.Show all products
        2.Choose a category
        3.Show my cart \n
        """)
        if chosen == '0':
            break
        elif chosen == '1':
            show_all_products()
        elif chosen == '2':
            choose_category()
        elif chosen == '3':
            show_cart()
        else:
            print ('Invalid number of operation')
