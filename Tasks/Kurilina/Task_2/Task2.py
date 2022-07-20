d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
while type:
    number_phone = input('Please, enter number phone\n')
    if len(number_phone) == 10:
       try:
           key_phone = int(number_phone)
       except:
          print("Please use only digits.Try again!")
       else:
          break
    else:
     print("Check your phone number, it must contain 10 digits.Try again!")  
a = d.get(key_phone, "the number was not found")
print(a) if type(a) == str else print (f'{a[0][0]} {a[0][1]} from {a[1][0]}, {a[1][1]}')

 