
import bl

flag = True

def wrong_input():
    print("Wrong enter.Try again, please!") 

def show_category_products(chose):
    print (bl.get_category_product(chose))

def show_all_products():
    print(bl.get_all_products())

def input_number():
    return input("""Enter:
    the NUMBER of product - to look information about it 
    the NAME of product - to do order
    "r" - to return in categories menu
    """)

      
def add_product():
    a = input_number()
    if a == 'r':
        categories()
    else:    
        print(bl.get_information(a))
     
def view_your_shopping_cart():
    print(bl.view_your_shopping_cart())

def clear_shopping_cart():
    print(bl.clearing())

def delete_product_from_shopping_cart():
    print(bl.view_your_shopping_cart())
    name = input("""Please,view your shopping cart and
    enter the name of product you want to del
    """)
    print(bl.delete_product(name))

def confirm_the_order():
    print(bl.view_your_shopping_cart())
    print(bl.find_sum())
    print("Thank you for choosing us! Have a good Day!")
    global flag
    flag = False

def start_menu():
    global flag
    while flag == True:
        answer = input("""Enter  the number of operation:
        1.add products in shopping cart
        2.delete products from shopping cart
        3.clear shopping cart
        4.view your shopping cart
        5.confirm the order
        6.show all products
        7.show category of products 
        """)
        if answer.isdigit() and int(answer) < 8 :
            if int(answer) > 0:
                if answer == "1":
                    categories()
                elif answer == '2':
                    delete_product_from_shopping_cart()
                elif answer == '3':
                    clear_shopping_cart()
                elif answer == '4':
                    view_your_shopping_cart()     
                elif answer == '5':
                    confirm_the_order()
                    break
                elif answer == '6':
                    show_all_products()
                elif answer == '7':   
                    categories()
            else: 
                 wrong_input()       
        else:
             wrong_input()            


def categories():
    global flag
    while flag == True:
        chosen = input("""Enter the number of category to look products you need:
        0.fruits and vegetables
        1.fish and seafood
        2.meat and poultry
        3.groceries
        4.confectionery
        5.cold drinks
        6.show me all products
        7.return to main menu
        """)
        if chosen.isdigit() and int(chosen) >=0:
            if chosen == '7':
                start_menu()
                break
            elif int(chosen) < 7:
                if int(chosen) < 6:
                    show_category_products(chosen)
                elif chosen == '6':
                    show_all_products()              
                add_product()
            else:    
                wrong_input()

        else:
            wrong_input()
            
           
             