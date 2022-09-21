import bl

def show_catalog():
    print(f"{bl.get_catalog()}")
    while True:
        choise = input ("""Enter the number of your operation:
        0.Exit
        1.Show notebook
        2.Show mobile phone
        3.Show watsh
        4.Show all catalog
    """)
        if choise == '0':
            break
        elif choise == '1':
            show_notebook() 
        elif  choise == '2':
            show_phone()
        elif choise == '3':
            show_watch()
        elif choise == '4':
            show_all_catalog() 
            break

def show_notebook():
    print(f"{bl.get_notebook()}")

def show_phone():
    print(f"{bl.get_phone()}")

def show_watch():
    print(f"{bl.get_watch()}")

def show_all_catalog():
    print(f"{bl.get_all_catalog()}")


def show_cart(name):
    print("--------------------")
    return bl.add_to_cart(name)

def make_an_order():
    while True: 
        item_for_order = input("Please, enter the correct name of the good you have chosen:\n")
        try:
            print (f'{show_cart(item_for_order)}')
            break
        except  Exception:
            print("Wrong name of the good")

def show_total_sum():
    print("--------------------------------------------------------------")
    return bl.total_sum()


while True:
    chosen = input("""Enter the number of your operation:
    0.Exit
    1.Show catalog
    2.Make an order
    """)

    if chosen == '0':
        break
    elif chosen == '1':
        show_catalog()
        choise = input("Do you want to continue? Please, enter 'Yes' or 'No'\n")
        if choise == "Yes":
         continue
        else:
            print("Thank you, see you soon!")
            break 

    elif chosen == '2':
        make_an_order()
        while True:
            o = input("Do you want to order? Please, enter 'Yes' or 'No'\n") 
            if o == "Yes":
                make_an_order()      
            elif o == "No":
                print(f"the total price is {show_total_sum()}. Thank you for your order")   
                print("--------------------------------------------------------------") 
                break 

    break    