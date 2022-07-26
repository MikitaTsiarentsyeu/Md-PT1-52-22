d = {
9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]
}

while True:
    n = input ('Please enter the phone number, 10 digits:\n')
    if n.isdigit() and len(n) == 10:
        n = int (n)          
        if n in d.keys():
            print(f'{d.get(n)[0][0]} {d.get(n)[0][1]} from {d.get(n)[1][0]}, {d.get(n)[1][1]}')
        else:
            print('The number was not found')
        break
    else:
        print('Incorrect input! Please enter exactly 10 digits and try again.')