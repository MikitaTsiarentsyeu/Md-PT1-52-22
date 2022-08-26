import bl

def show_all_contacts():
    print(bl.get_all_contacts())

def input_name():
    return input("input a name:\n")

def input_phones():
    return input("input your phones divided by a comma:\n")

def add_contact():
    print(bl.add_contact(input_name(), input_phones())) 

def remove_contact():
    print(bl.remove_contact(input_name()))

def remove_phones():
    print(bl.remove_phones(input_name(), input_phones()))

# def add_phones():
#     print(bl.add_phones(input_name(), input_phones())) 

def start_main_flow():
    while True:
        chosen = input("""Enter the number of your operation:
        0.Exit
        1.Show all contacts
        2.Add contact
        3.Add phones to a contact
        4.Remove a contact
        5.Remove phones from a contact
        """)

        if chosen == '0':
            break
        elif chosen == '1':
            show_all_contacts()
        elif chosen == '2':
            add_contact()
        elif chosen == '3':
            add_contact()
        elif chosen == '4':
            remove_contact()
        elif chosen == '5':
            remove_phones()