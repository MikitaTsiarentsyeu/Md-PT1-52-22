import data

def get_all_contacts():
    contacts = data.get_all_contacts()
    return '\n'.join([f"{c}: {','.join(n)}" for c, n in contacts.items()])

def add_contact(name, phones):
    correct_phones = []
    incorrect_phones = []
    for phone in phones.split(','):
        if validate_phone(phone):
            correct_phones.append(phone)
        else:
            incorrect_phones.append(phone)
    res = data.add_contact(name, *correct_phones)
    phones_message = "all phones were added"
    if len(incorrect_phones) > 0:
        phones_message = f"phones {','.join(correct_phones)} added, phones {','.join(incorrect_phones)} skipped because of incorrect phone format"
    contact_message = "the contact was created"
    if not res:
        contact_message = "the contact was updated"
    return f"{contact_message}, {phones_message}"

def remove_contact(name):
    if data.remove_contact(name):
        return "the contact was removed"
    else:
        return "the contact does not exist"

def remove_phones(name, phones):
    res = data.remove_phones(name, *phones.split(','))
    if not res:
        return "the contact does not exist or it has no such numbers"
    if len(phones) == len(res):
        return "all phones were deleted"
    else:
        return f"{','.join(res)} were deleted"

def validate_phone(phone):
    if len(phone) == 7 and phone.isdigit():
        return True
    return False