import data

def get_catalog():
    l = data.get_catalog()
    return '  |  '.join(l.keys())


def get_notebook():
    l = data.get_catalog()
    notebook = l.get("notebook")
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in notebook.items()])

def get_phone():   
    l = data.get_catalog() 
    phone = l.get("phone")  
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in phone.items()])

def get_watch():
    l = data.get_catalog()
    watch = l.get("watch")  
    return '\n'.join([f"{item}: {' | '.join([f'{k} -> {v}' for k, v in value.items()])}" for item, value in watch.items()])

def get_all_catalog():
    return (f"{get_notebook()}\n{get_phone()}\n{get_watch ()}")

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