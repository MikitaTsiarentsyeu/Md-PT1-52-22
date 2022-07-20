data = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

x = input ('Please enter your name:\n')
print ('Hello,', x, end = '!\n')
phone = input('Please enter 10 digit phone number\n')
if phone.isdigit(): 
    if len(phone) == 10:
        phone = int(phone)
        if phone in data.keys():
            print(f'Name: {data.get(phone)[0][0]} {data.get(phone)[0][1]}. From: {data.get(phone)[1][0]}, {data.get(phone)[1][1]}.')
    elif len(phone) != 10:
        print('The value should contain 10 numbers')
else:
    print ('Incorrect input, try again')



