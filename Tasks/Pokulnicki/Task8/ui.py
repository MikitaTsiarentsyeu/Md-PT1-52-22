import bl

def show_position(number):
    print("===============================================================================================")
    print(bl.get_position(number))
    print("===============================================================================================")

def start_main_flow():
    print("===============================================================================")
    print("                        WELCOM TO OUR STORE                                    ")
    print("===============================================================================")
    while True:
        chosen = input("""Enter the number of your operation:
    0.Exit
    1.Show all product
    2.Show product by category
    3.Open cart
    4.Show your deposit
    5.Increase Deposit \n""")
        if chosen == '0':
            break
        elif chosen == '1':
            show_position(0)
            while True:
                chosen = input("""If you want to add product to your cart, enter the "Product Code". 
To return to the main menu, enter 0:

    0.Back to main menu
    (Product code). To add product to cart \n""")
                if chosen == '0':
                    break
                elif chosen.isdigit():
                    show_position(0)
                    response = bl.add_in_cart(int(chosen))
                    print("=================================================================")
                    print(f"                 {response}                    ")
                    print("=================================================================")
        
        elif chosen == '2':
            while True:
                chosen = input("""Enter the number of your operation:
        0.Back to main menu
        1.Mobilefone
        2.Notebook
        3.Watch \n""")
                if chosen == '0':
                    break
                elif chosen == '1':
                    show_position(1)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Product Code". 
To return to the main menu, enter 0:

    0.Back to main menu
    (Product code). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(1)
                            response = bl.add_in_cart(int(chosen))
                            print("=================================================================")
                            print(f"                 {response}                    ")
                            print("=================================================================")
                elif chosen == '2':
                    show_position(2)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Product Code". 
To return to the main menu, enter 0:

    0.Back to main menu
    (Product code). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(2)
                            response = bl.add_in_cart(int(chosen))
                            print("=================================================================")
                            print(f"                 {response}                    ")
                            print("=================================================================")
                elif chosen == '3':
                    show_position(3)
                    while True:
                        chosen = input("""If you want to add product to your cart, enter the "Product Code". 
To return to the main menu, enter 0:

    0.Back to main menu
    (Product code). To add product to cart \n""")
                        if chosen == '0':
                            break
                        elif chosen.isdigit():
                            show_position(3)
                            response = bl.add_in_cart(int(chosen))
                            print("=================================================================")
                            print(f"                 {response}                    ")
                            print("=================================================================")
        elif chosen == '3':
            print("===============================================================================================")
            print("              YOU CART                  ")
            print(bl.get_shopping_cart())
            print("===============================================================================================")
            print(f"Total price {bl.get_price()}$" )
            print("===============================================================================================")
            print(f"You deposit is {bl.get_deposit()}$")
            while True:
                chosen = input("""Enter the number of your operation:
    0.Back to main menu
    1.Buy product
    2.Remove product from the cart\n""")
                if chosen == '0':
                    break
                elif chosen == '1':
                    print("=================================================================")
                    print("Thank you so much for the purchase")
                    print("=================================================================")
                    bl.set_deposit(-bl.get_price())
                    print("=================================================================")
                    print(f"You deposit is {bl.get_deposit()}$")
                    print("=================================================================")
                    bl.clean_cart()
                    break
                elif chosen == '2':
                    print("===============================================================================================")
                    print("              YOU CART                  ")
                    print(bl.get_shopping_cart())
                    print("===============================================================================================")
                    print(f"Total price {bl.get_price()}$" )
                    print("===============================================================================================")
                    print(f"You deposit is {bl.get_deposit()}$")                    
                    while True:
                        chosen = input("""Enter the number of position for remove:
    0.Back to main menu
    №.Remove product from cart \n""")
                        if chosen.isdigit() and 0 <= int(chosen) < bl.count_cart() :
                            bl.remove_product(chosen)
                            print("===============================================================================================")
                            print("              YOU CART                  ")
                            print(bl.get_shopping_cart())
                            print("===============================================================================================")
                            print(f"Total price {bl.get_price()}$" )
                            print("===============================================================================================")
                            print(f"You deposit is {bl.get_deposit()}$")
                            break    
                        else:
                            print("===============================================================================================")
                            print("This possition no is cart")
                            print("===============================================================================================")


        elif chosen == '4':
            print("======================")
            print(f"You deposit is {bl.get_deposit()}$")
            print("======================")
        elif chosen == '5':
            while True:
                chosen = input(""" Enter the amount you want to deposit \n""")
                if chosen.isdigit() and int(chosen) >= 0:
                    bl.set_deposit(int(chosen))
                    print("======================")
                    print(f"You deposit is {bl.get_deposit()}$")
                    print("======================")
                    break
                else:
                    print("Enter a non-negative numer")


            
