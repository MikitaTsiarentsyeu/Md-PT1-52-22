import data

def get_all_contacts():
    contacts = data.get_all_contacts()
    return '\n'.join([f"{c}: {','.join(n)}" for c, n in contacts.items()])

def add_contact(name, phones):
    #validate phones!
    data.add_contact(name, *phones.split(','))
    return f"The new contact was created:\n{get_all_contacts()}"