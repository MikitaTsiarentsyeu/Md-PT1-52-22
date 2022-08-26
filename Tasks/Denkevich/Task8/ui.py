import bl


def show_all_categories():
    return print(bl.get_all_categories())


def show_goods_from_category(name):
    return bl.get_goods_from_category(name)


def refresh_the_cart(name, n):
    return bl.minus_in_cart(name, n)


def show_cart():
    return bl.get_cart()


def show_serials():
    print(f"{bl.compact_serials()}\n")


def order_finish():
    bl.balance_reducing()
    bl.prepare_cart_and_sum()
    return print("Order is successfully finished.")


def order_pay(name, n):
    return bl.full_sum(name, n)


def show_balance():
    b = bl.wallet_balance()
    return print(f"Your balance is {b}")


def show_total_payment():
    return print(f"Total payment is: {bl.total_payment()} $")


print("\n")
while True:
    show_balance()
    show_total_payment()
    n = input("""0. Exit
1. Show categories of goods
2. Show cart
3. Order checkout\n
""")
    if n == "0":
        print("Thank you. Come again. =)\n")
        break
    elif n == "1":
        show_all_categories()
        n = input("""
0. Back
1. Choose a broduct to buy
2. View serial numbers of goods\n
""")
        if n == "0":
            continue
        elif n == "1":
            name = input("""
- Please, enter a category name
  or press ENTER to view the whole assortment.
(0. To main menu)\n
""")
            if name == "0":
                continue
            if show_goods_from_category(name) == None:
                print("Incorrect, try again.\n")
                continue
            else:
                print(show_goods_from_category(name))
                try:
                    name_n = input("""
- Buy something?
  Enter the name of product and number of it by a space.
(0. To main menu)\n
""")
                    if name_n == "0":
                        continue
                    else:
                        name = name_n.split(" ")[0]
                        n = int(name_n.split(" ")[1])
                        if bl.if_sum_exeeding(name, n) == -1:
                            print("\nYou have no money to pay for it, sory.\n")
                            continue
                        elif refresh_the_cart(name, n) == -1:
                            print(
                                "The store dosen't contain such number of this product\n")
                            continue
                        else:
                            order_pay(name, n)
                            print("""
- Done.
  Check your cart.\n""")
                except:
                    print("Incorrect, try again.\n")
                    continue
        elif n == "2":
            show_serials()
        else:
            print("Incorrect, try again.\n")
            continue
    elif n == "2":
        if show_cart() == -1:
            print("Empty.\n")
        else:
            print(f"{show_cart()}\n")
    elif n == "3":
        if show_cart() == -1:
            print("""
Your cart is empty.
Add something.\n""")
            continue
        else:
            order_finish()
            print("\n")
    else:
        print("Incorrect, try again.\n")
        continue
