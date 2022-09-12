import data

def get_catalog():
    l = data.get_catalog()
    return '  |  '.join(l.keys())
            

def get_cell_phones():
    l = data.get_catalog()
    cell_phones = l.get("Cell phones")
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in cell_phones.items()])
    
def get_headphones():   
    l = data.get_catalog() 
    headphones = l.get("Headphones")  
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in headphones.items()])

def get_loudspeakers():
    l = data.get_catalog()
    loudspeakers = l.get("Loudspeakers")  
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in loudspeakers.items()])

def get_all_goods():
    return (f"{get_cell_phones()}\n{get_headphones()}\n{get_loudspeakers ()}")


cart = []
def add_to_cart(name):
    res = data.find(name)
    cart.append(res)   
    return "\n".join(cart)

def total_sum():
    sum = 0
    for string in cart:
        for word in string.split(' '):
            if "$" in word:
                word =word[:-1]
                sum = sum + int(word)
    return f"{sum}$"


   
 



