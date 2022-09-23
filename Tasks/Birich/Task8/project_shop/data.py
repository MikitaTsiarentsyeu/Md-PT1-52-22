cart = {}

products = {
    "Auto": {"Range Rover": ["0011", "231999.99", "5"], "Volvo": ["0022", "75999.97", "12"], "Jaguar": ["0033", "93999.97", "8"]},
    "Car tires": {"Cordiant": ["0100", "68.99", "120"], "Michelin": ["0200", "122.97", "43"], "Nexen": ["0300", "64.99", "34"]},
    "Smart House": {"Smart lamps": ["1010", "12.99", "1040"], "Smart speakers": ["1020", "23.99", "101"], "Smart sockets": ["1030", "13.99", "350"]}
}


def get_all_products():
    return products


def get_all_categories():
    return products


def get_products():
    return products


def get_add_products(add_prod):
    for i in products.keys():
        for e in products[i].keys():
            if add_prod == e:
                cart[e] = products[i][e]
                return True
    return False
