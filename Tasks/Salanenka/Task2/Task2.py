dict = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")], 4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")], 6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")], 7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
while True: 
    input_number = input ("Enter the phone number in 1234567890 format: \n")
    if (input_number.isdigit()) == False or len(input_number) != 10:
        print ('Error.Try again')
    else:
        input_number = int(input_number)
        number = dict.get(input_number)
        if number == None:
            print ("The number was not found")
        else:
            contact, place = number[0], number[1]
            name, surname = contact[0], contact[1]
            city, state = place[0], place[1]
            output = f'{name} {surname} from {city},{state}'
            print (output)
        break
 