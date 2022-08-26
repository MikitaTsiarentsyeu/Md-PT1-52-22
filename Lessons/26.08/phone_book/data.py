repo = {"some name":["85252765788", "7657858789"], "another name": ["486465135168"]}

def get_all_contacts():
    return repo

def add_contact(name, *phones):
    if name in repo:
        repo[name].extend(phones)
        repo[name] = list(set(repo[name]))
        return False
    else:
        repo[name] = list(phones)
        return True


# def add_phone(name, phone): pass

def remove_contact(name):
    if name in repo:
        del repo[name]
        return True
    return False

def remove_phones(name, *phones):
    res = []
    if name in repo:
        for phone in phones:
            if phone in repo[name]:
                repo[name].remove(phone)
                res.append(phone)
        return res
    else:
        return False

