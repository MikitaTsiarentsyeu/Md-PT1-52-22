data_shop_fender = {1001:["fender","Fender Stratocaster",1200,15],
                        1002:["fender","Fender Telecaster",1200,18],
                        1003:["fender","Fender Jaguar",1700,10],
                        1004:["fender","Fnder Jazzmaster",1700,10]}

data_shop_gibson = {2001:["gibson","Gibson Les Paul",2000,7],
                        2002:["gibson","Gibson SG",2000,6],
                        2003:["gibson","Gibson Flying V",1800,10]}

data_shop_ibanez = {3001:["ibanez","Ibanez S521-BBS",800,20],
                        3002:["ibanez","Ibanez S6570SK-STB",700,23],
                        3003:["ibanez","Ibanez RG421 MOL",900,27],
                        3004:["ibanez","Ibanez GIO GRG7221QA-TKS",600,22]}

data_shop_jackson = {4001:["jackson","Jackson JS1X RR",500,29],
                        4002:["jackson","Jackson JS32",600,28],
                        4003:["jackson","Jackson JS11",800,30],
                        4004:["jackson","Jackson JS22-7",700,31]}

data_shop_yamaha = {5001:["yamaha","Yamaha PAC-112",400,43],
                        5002:["yamaha","Yamaha Pacifica 012",200,42],
                        5003:["yamaha","Yamaha RGX-121Z",300,35]}

data_shop_gretsch = {6001:["gretsch"," Gretsch G5426",500,28],
                        6002:["gretsch","Gretsch G2217",600,27],
                        6003:["gretsch","Gretsch G5435T",600,25],
                        6004:["gretsch","Gretsch G2210",500,26]}

shopping_cart = []
shopping_cart_temp = []
deposit = 1000
count = 0

def get_position(): 
    return data_shop_fender, data_shop_gibson, data_shop_ibanez, data_shop_jackson, data_shop_yamaha, data_shop_gretsch

def add_in_cart(p_number,name_of_base):
    shopping_cart_temp.append(name_of_base.get(p_number))
    name_of_base.get(p_number)[3] = name_of_base.get(p_number)[3] - 1
    global count
    temp = name_of_base.get(p_number).copy()
    temp.insert(0,count)
    shopping_cart.append(temp)
    count +=1


def get_shopping_cart():
    return shopping_cart

def get_deposit():
    return deposit

def set_deposit(number):
    global deposit 
    deposit = deposit + number

def get_price():
    temp = sum([p[3] for p in shopping_cart])
    return temp

def clean_cart():
    shopping_cart.clear()
    global count
    count = 0

def remove_product(number):
    shopping_cart.pop(number)
    global count 
    count -=1
    for x in range(len(shopping_cart)):
        shopping_cart[x][0] = x
    shopping_cart_temp[number][3] = shopping_cart_temp[number][3] +1
    shopping_cart_temp.pop(number)

def count_cart():
    return len(shopping_cart)