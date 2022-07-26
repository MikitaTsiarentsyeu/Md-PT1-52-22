

user = {9103976271: [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
        4199392609: [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
        9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
        6123479367: [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
        7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

user_phone = input("\nPlease write a 10-digit number: ")

if user_phone.isdigit() == True and len(user_phone) == 10:
    user_data = user.get(int(user_phone))
    if user_data in user.values():
        print(
            f"\n{user_data[0][0]} {user_data[0][1]} from {user_data[1][0]}, {user_data[1][1]}\n")
    else:
        print("\nthe number was not found")
else:
    print("\nThe phone data is entered incorrectly!\nPlease be careful.")
