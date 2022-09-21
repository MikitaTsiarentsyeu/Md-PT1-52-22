catalog = {
    "notebook": {"MacBook Air": {"Code":"215-1325", "Price":"1999$", "Stock":"10"}, "Sony VAIO E17":{"Code":"003-515", "Price":"1500$", "Stock":"5"}},
    "phone": {"Iphone 14":{"Code":"515-985", "Price":"799$", "Stock":"15"},"Huawei P50":{"Code":"517-000", "Price":"500$", "Stock":"16"} },
    "watch": {"AppleWatch Series 8":{"Code":"000-005", "Price":"399$", "Stock":"8"}, "Huawei FIT":{"Code":"366-999", "Price":"150$", "Stock":"25"}}
}

def get_catalog():
    return catalog

def find(name):
    for main_value in catalog.values():
        for key in main_value.keys():
            if key == name:
                res = str(f'{key} : {main_value.get(name).get("Price")}')
                return res