i = True
while i:
    try:
        buch = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
        4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
        9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
        6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
        7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
        a = (input('Enter the number to search for data \n'))
        c = str(a).replace(' ', '')
        z = len(str(c))
        q = str(a).replace(' ', '').isdigit()
        print(z)
        if q == True or z != 10:
            v = int(c)
            print(' Surname: '+ buch[v][0][0]+'\n' ,'Forename: '+ buch[v][0][1]+'\n',
            'City: '+ buch[v][1][0]+'\n','State: '+ buch[v][1][1])
    except KeyError:
        print(('Error: You did not enter a correct number'))
    except Exception as x:
        print('Unknown error: Please enter the phone number in numbers '
          'without other characters and spaces to find out the information\n', x)
    i = True if input('Restart the program 1(Yes)/2(No)') == '1' else False

