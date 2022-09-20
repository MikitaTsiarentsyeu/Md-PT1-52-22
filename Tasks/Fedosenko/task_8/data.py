
catalog = {
    "Cell phones":{
            "iPhone 13":{
            "HS-code":"123-000",
            "Price":"1000$",  
            "Stock quantity": "10"
            },

            "iPhone 12":{
            "HS-code":"223-100",
            "Price":"900$",  
            "Stock quantity": "7"
            } },

    "Headphones":{
            "Airpods 2":{
            "HS-code":"555-000",
            "Price":"200$",  
            "Stock quantity": "20"
            }, 
            "Airpods 3":{
            "HS-code":"588-100",
            "Price":"250$",  
            "Stock quantity": "15"
            } },

    "Loudspeakers":{
            "JBL Flip 5":{
            "HS-code":"485-009",
            "Price":"180$",  
            "Stock quantity": "3"
            },
            "JBL Flip 4":{
            "HS-code":"385-099",
            "Price":"140$",  
            "Stock quantity": "1"
            }  
    }}

def get_catalog():
    return catalog


def find(name):
    for main_value in catalog.values():
        for key in main_value.keys():
            if key == name:
                res = str(f'{key} : {main_value.get(name).get("Price")}')
                return res
