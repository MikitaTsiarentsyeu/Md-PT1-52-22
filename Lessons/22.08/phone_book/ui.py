import bl

def show_all_contacts():
    print(bl.get_all_contacts())

def input_name():
    return input("input new name:\n")

def input_phones():
    return input("input your phones divided by a comma:\n")

def add_contact():
    print(bl.add_contact(input_name(), input_phones())) 

while True:
    chosen = input("""Enter the number of your operation:
    0.Exit
    1.Show all contacts
    2.Add contact
    """)

    if chosen == '0':
        break
    elif chosen == '1':
        show_all_contacts()
    elif chosen == '2':
        add_contact()