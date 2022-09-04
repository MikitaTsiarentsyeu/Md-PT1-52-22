
import data

def get_all_products(): 
    products = data.get_all_products()
    mas = []
    for i in products.keys():
        for a in products[i].keys():
            mas.append(f'{products[i][a][0]}.{a}')
   
    return '\n'.join(mas)    

def get_category_product(chose):
    category = data.get_category_product(chose)  
    return '\n'.join([f'{category[i][0]}.{i}' for i in category.keys()])
    
def get_information(number):
    catalog = data.get_all_products()
    if number.isdigit():    
        if int(number) in data.numbers:
            for i in catalog.keys():
                for a in catalog[i].keys():
                    if catalog[i][a][0] == number:
                        return f'name - {a}; '+'{}'.join(catalog[i][a]).format(' - number; ',' - price,BYN; ') + ' - account in stock.'
    else:
         return add_product(number)
    

def clearing():
    if data.clearing():
        return "The shopping cart is cleared"
    return "The shopping cart is empty"  

def view_your_shopping_cart():
    shopping_cart = data.view_your_shopping_cart()
    if shopping_cart:
        return f'Your order is:\n'+ '\n'.join([f'name - {i}; '+'{}'.join(shopping_cart[i]).format(' - number; ',' - price,BYN; ') + ' - account in stock.' for i in shopping_cart.keys()]) 
    return "The shopping cart is empty"   

def find_sum():
    shopping_cart = data.view_your_shopping_cart()
    return f'The amount of your order is {sum([int(shopping_cart[i][1]) for i in shopping_cart.keys()])} BYN'
        
def delete_product(name):
    if data.delete_product(name):
        return "The product is deleted"
    return "There is no such product in your shopping cart.Check your input and try again!"    
    
def add_product(adding):
    if data.add_product(adding):
        return "Your product is added in your shopping cart!"
    return "There is no such product in our shop.Check your input and try again!"    
        

