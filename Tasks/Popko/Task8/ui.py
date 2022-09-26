import bl

def show_position(number):
    print(bl.get_position(number))

def start_main_flow():
    print("Welcome to Python Guitar! We sell electric guitars all tastes")
    while True:
        chosen = input("""Enter the number of your operation:
    0.Exit
    1.Show all product
    2.Show product by brand
    3.Open cart
    4.Show your deposit
    5.Increase Deposit \n""")
        if chosen == '0':
            break
        elif chosen == '1':
            show_position(0)
            while True:
                chosen = input("""If you want to put product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                if chosen == '0':
                    break
                elif chosen.isdigit():
                    show_position(0)
                    response = bl.add_in_cart(int(chosen))
                    print(f"{response}")

        elif chosen == '2':
            while True:
                chosen = input("""Enter the number of your operation:
        0.Back to main menu
        1.Fender
        2.Gibson
        3.Ibanez
        4.Jackson
        5.Jamaha
        6.Gretsch \n""")
                if chosen == '0':
                    break
                elif chosen == '1':
                    show_position(1)
                    while True:
                        chosen = input("""If you want to put product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To put product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(1)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
                elif chosen == '2':
                    show_position(2)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(2)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
                elif chosen == '3':
                    show_position(3)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(3)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
                elif chosen == '4':
                    show_position(2)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(4)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
                elif chosen == '5':
                    show_position(2)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(5)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
                elif chosen == '6':
                    show_position(2)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Code of product". 
To return to the main menu, enter 0:
    0.Back to main menu
    (Code of product). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(6)
                            response = bl.add_in_cart(int(chosen))
                            print(f"{response}")
        elif chosen == '3':
            print("Your cart")
            print(bl.get_shopping_cart())
            print(f"Total price {bl.get_price()}$" )
            print(f"You deposit is {bl.get_deposit()}$")
            while True:
                chosen = input("""Enter the number of your operation:
    0.Back to main menu
    1.Buy product
    2.Remove product from the cart\n""")
                if chosen == '0':
                    break
                elif chosen == '1':
                    print("Thank you so much for the purchase")
                    bl.set_deposit(-bl.get_price())
                    print(f"You deposit is {bl.get_deposit()}$")
                    bl.clean_cart()
                    break
                elif chosen == '2':
                    print("Your cart")
                    print(bl.get_shopping_cart())
                    print(f"Total price {bl.get_price()}$" )
                    print(f"You deposit is {bl.get_deposit()}$")                    
                    while True:
                        chosen = input("""Enter the number of position for remove:
    0.Back to main menu
    №.Remove product from cart \n""")
                        if chosen.isdigit() and 0 <= int(chosen) < bl.count_cart() :
                            bl.remove_product(chosen)
                            print("Your cart")
                            print(bl.get_shopping_cart())
                            print(f"Total price {bl.get_price()}$" )
                            print(f"You deposit is {bl.get_deposit()}$")
                            break    
                        else:
                            print("This possition no is cart")
        elif chosen == '4':
            print(f"You deposit is {bl.get_deposit()}$")
        elif chosen == '5':
            while True:
                chosen = input("Enter the amount you want to deposit \n")
                if chosen.isdigit() and int(chosen) >= 0:
                    bl.set_deposit(int(chosen))
                    print(f"You deposit is {bl.get_deposit()}$")
                    break
                else:
                    print("Enter a non-negative numer")()