
shopping_cart = {}

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
categories  =['fruits and vegetables','fish and seafood','meat and poultry','groceries','confectionery','cold drinks']
catalog = {'fruits and vegetables':{'potatoes': ['001','10','5'], 'tomatoes': ['002','10','4'], 'peppers': ['003','11','6']},
            'fish and seafood':{'shrimp' : ['004','12','9'], 'perch': ['005','15','8'], 'squid': ['006','19','5']},
            'meat and poultry':{'chicken': ['007','15','9'], 'pork': ['008','11','8'], 'beef': ['009','11','5']},
            'groceries':{'flour': ['010','12','9'], 'salt': ['011','13','8'], 'sugar': ['012','8','5']},
            'confectionery':{'chocolate': ['013','35','9'], 'cake': ['014','18','8'], 'candy': ['015','15','5']},
            'cold drinks':{'schweppes': ['016','21','9'], 'cola': ['017','16','8'], 'juice': ['018','12','5']}}

def get_all_products(): 
    return catalog

def get_category_product(chose):
    return catalog[categories[int(chose)]]

def clearing():
    if shopping_cart:
       shopping_cart.clear()
       return True   
    return False

def view_your_shopping_cart():
    if shopping_cart:
        return shopping_cart
    return False        

def delete_product(name):
    if name in shopping_cart:
        del shopping_cart[name]
        return True
    return False       

def add_product(adding):
    for i in catalog.keys():
        for t in catalog[i].keys():
            if adding == t:
                shopping_cart[t] = catalog[i][t]
                return True 
    return False

