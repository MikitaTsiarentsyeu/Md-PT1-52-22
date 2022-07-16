d = {9103976271:[("Rehina", "Meinhard"),("Memphos", "Tennessee")],
4199392609:[("Stephonie", "Bruse"),("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takya"),("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

n = input("Enter the phone number:\n")

if (n.isdigit()):
    if (len(n) > 10):
        print('To long number.')
    elif (len(n) < 10):
        print('To short number.')
    else:
        if (n == '9103976271'):
            print(f"{{{d.get(int(n))[0][0]}}} {{{d.get(int(n))[0][1]}}} from {{{d.get(int(n))[1][0]}}}, {{{d.get(int(n))[1][1]}}}")
        elif (n == '4199392609'):
            print(f"{{{d.get(int(n))[0][0]}}} {{{d.get(int(n))[0][1]}}} from {{{d.get(int(n))[1][0]}}}, {{{d.get(int(n))[1][1]}}}")
        elif (n == '9099459979'):
            print(f"{{{d.get(int(n))[0][0]}}} {{{d.get(int(n))[0][1]}}} from {{{d.get(int(n))[1][0]}}}, {{{d.get(int(n))[1][1]}}}")
        elif (n == '6123479367'):
            print(f"{{{d.get(int(n))[0][0]}}} {{{d.get(int(n))[0][1]}}} from {{{d.get(int(n))[1][0]}}}, {{{d.get(int(n))[1][1]}}}")
        elif (n == '7548993768'):
            print(f"{{{d.get(int(n))[0][0]}}} {{{d.get(int(n))[0][1]}}} from {{{d.get(int(n))[1][0]}}}, {{{d.get(int(n))[1][1]}}}")   
        else:
            print('The number was not found.')
else:
    print('Please enter only figures.')