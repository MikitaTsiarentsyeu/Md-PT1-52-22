import bl


def show_all_products():
    print(bl.get_all_products())


def show_all_categories():
    print(bl.get_all_categories())


def show_products(user_chose):
    print(bl.get_products(user_chose))


def show_add_products(add_prod):
    print(bl.get_add_products(add_prod))


def show_buy_products():
    print(bl.get_buy_product())


def watch_add_products():
    while True:
        choice_user = input("""
    --> Exit cart -> 0
    --> Add to Basket -> 1
    --> Make a purchase -> 2 \n""")
        if choice_user == "0":
            break
        elif choice_user == "1":
            show_all_products()
            show_add_products(choice_user)
            continue
        elif choice_user == "2":
            show_buy_products()
            break
        else:
            print("\nYou entered incorrect data, please try again!")
        continue


def watch_choice_category():
    while True:
        show_all_categories()
        choice_user = input("""
    --> Leave category -> 0
    --> Category "Auto" -> 1
    --> Category "Car tires" -> 2
    --> Category "Smart House" -> 3
    Enter the selected category: \n""")
        if choice_user == "0":
            break
        elif choice_user == "1":
            show_products("Auto")
        elif choice_user == "2":
            show_products("Car tires")
        elif choice_user == "3":
            show_products("Smart House")
        else:
            print("\nYou entered incorrect data, please try again!")
        continue


def start_main_flow():
    while True:
        input_user = input("""\n"OnlineR" --> find your happiness!
    --> Leave the store -> 0
    --> View all products -> 1
    --> View product categories -> 2
    --> Add item to cart -> 3
    --> Make a purchase -> 4
    Enter data for the selected field: \n""")
        if input_user == "0":
            show_buy_products()
            print("Thanks for choosing, with love 'OnlineR'!\n")
            break
        elif input_user == "1":
            show_all_products()
        elif input_user == "2":
            watch_choice_category()
        elif input_user == "3":
            show_all_products()
            show_add_products(input_user)
            watch_add_products()
        elif input_user == "4":
            show_all_products()
            show_add_products(input_user)
            watch_add_products()
        else:
            print("\nYou entered incorrect data, please try again!")
        continue
