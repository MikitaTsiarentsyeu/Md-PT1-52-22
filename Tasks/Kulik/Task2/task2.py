
d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]} 

phone = input("Enter phone number:\n")
if phone.isdigit():
    if (len(phone) != 10):
        print("Error, input 10 digits:\n")
    else:
            phone = int(phone)
    if phone in d.keys():
       print(f'{d.get(phone)[0][0]} {d.get(phone)[0][1]} from {d.get(phone)[1][0]} {d.get(phone)[1][1]}')
    else:
        print("This number is not in the database")
else:
    print("Enter only numbers:\n") 