repo = {"some name":["85252765788", "7657858789"], "another name": ["486465135168"]}

def get_all_contacts():
    return repo

def add_contact(name, *phones):
    if name in repo:
        repo[name].extend(phones)
        repo[name] = list(set(repo[name]))
    else:
        repo[name] = list(phones)


# def add_phone(name, phone): pass

def remove_contact(name, phone): pass

def remove_phone(name, phone): pass

