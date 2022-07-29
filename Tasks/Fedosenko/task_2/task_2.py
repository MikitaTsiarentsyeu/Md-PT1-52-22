d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
while True:
    try:
        print('Please, enter a phone number: ')
        phone_number = int(input())
        if len(str(phone_number)) != 10:
            raise Exception()
        break
    except Exception as e:
        print("Incorrect format")    

if phone_number  in d:
  info = d.get(phone_number)
  name = info[0]
  first_name = name[0]
  last_name = name[1]
  address = info[1]
  city = address[0]
  state = address[1]
  print(f'{first_name} {last_name} from {city}, {state}') 

else:
    print('The number was not found')
