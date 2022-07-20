dictionary = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

phone_number = input('Please, enter the phone number: ')
if phone_number.isdigit():
    if (len(phone_number) != 10):
        print ('Error! Please, enter a number which consist of 10 digits.')
    else:
        phone_number = int(phone_number)
        if phone_number in dictionary.keys():
            print(f'Name: {dictionary.get(phone_number)[0][0]} {dictionary.get(phone_number)[0][1]}. From: {dictionary.get(phone_number)[1][0]}, {dictionary.get(phone_number)[1][1]}.')
        else:
            print('The number was not found.')
else:
    print('Error! The phone number must consist of only digits. Please, try again!')


