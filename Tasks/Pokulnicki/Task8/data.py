
shop_data_mobilefone = {1001:["mobilefone","Samsung A51",350,100],
                        1002:["mobilefone","Xiaomi Redmi Note 11",280,24],
                        1003:["mobilefone","iPhone 13",1000,11],
                        1004:["mobilefone","Huawei P50",980,24]}

shop_data_notebook = {2001:["notebook","Honor MagicBook",1235,234],
                        2002:["notebook","Lenovo IdeaPad",480,16],
                        2003:["notebook","HP ProBook",1430,17],
                        2004:["notebook","Huawei MateBook",1800,98]}

shop_data_watch = {3001:["watch","Huawei Watch GT",700,78],
                        3002:["watch","Apple Watch",789,44],
                        3003:["watch","Samsung Galaxy Watch",350,12],
                        3004:["watch","Xiaomi Mi Watch",50,900]}

shopping_cart = []
shopping_cart_temp = []
deposit = 10000
count = 0

def get_position():
    return shop_data_mobilefone, shop_data_notebook, shop_data_watch

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

