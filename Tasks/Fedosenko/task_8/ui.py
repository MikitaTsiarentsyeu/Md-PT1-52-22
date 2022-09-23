
import bl

def show_catalog():
    print("---------------------------------------------")
    print(f"{bl.get_catalog()}")
    print("---------------------------------------------")
    while True:
        choise = input ("""Enter the number of your operation:
        0.Exit
        1.Show cell phones
        2.Show headphones
        3.Show loudspeakers
        4.Show all goods
    """)
        if choise == '0':
            break
        elif choise == '1':
            show_cell_phones() 
        elif  choise == '2':
            show_headphones()
        elif choise == '3':
            show_loudspeakers()
        elif choise == '4':
            show_all_goods() 
            break

       
def show_cell_phones():
    print("--------------------------------------------------------------")
    print(f"{bl.get_cell_phones()}")
    print("--------------------------------------------------------------") 

def show_headphones():
    print("--------------------------------------------------------------")
    print(f"{bl.get_headphones()}")
    print("--------------------------------------------------------------") 

def show_loudspeakers():
    print("--------------------------------------------------------------")
    print(f"{bl.get_loudspeakers()}")
    print("--------------------------------------------------------------") 

def show_all_goods():
    print("--------------------------------------------------------------")
    print(f"{bl.get_all_goods()}")
    print("--------------------------------------------------------------") 

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
            print("Thank you! See you soon!")
            break 
        
    
    elif chosen == '2':
        make_an_order()
        while True:
            o = input("Do you want to order somethin else? Please, enter 'Yes' or 'No'\n") 
            if o == "Yes":
                make_an_order()      
            elif o == "No":
                print(f"the total price is {show_total_sum()}. Thank you for your order")   
                print("--------------------------------------------------------------") 
                break 
            
    break     
    
    