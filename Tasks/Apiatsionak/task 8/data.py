cart = {}

products = {
    "Phones": {"iPhone": ["0015", "2500", "7"], "Galaxy S22": ["0023", "2500", "14"], "Huawei": ["0045", "1500", "10"]},
    "Watches": {"Apple Watch": ["0100", "800", "120"], "Samsung Watch": ["0200", "700", "43"], "Huawei": ["0300", "400", "39"]},
    "Laptops": {"Macbook air": ["1020", "4000", "1047"], "Glaxy Book": ["1030", "3800", "107"], "Asus": ["1040", "2400", "360"]}
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