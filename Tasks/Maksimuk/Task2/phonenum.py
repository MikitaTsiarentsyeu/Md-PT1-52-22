d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
phone_number = input("Enter your phone number:\n")
if phone_number.isdigit() and len(phone_number) == 10:
    phone_number = int(phone_number)
    if phone_number in d.keys():
        print(f'{d.get(phone_number)[0][0]} {d.get(phone_number)[0][1]} from {d.get(phone_number)[1][0]}, {d.get(phone_number)[1][1]}.')
    else:
        print("the number was not found")
else:
    print("the number is incorrect")