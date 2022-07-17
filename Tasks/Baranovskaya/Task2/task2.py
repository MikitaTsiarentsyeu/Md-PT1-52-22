phonebook = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")], 
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")], 
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")], 
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")], 
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number = input("Please, enter the phone number:\n")

if number.isdigit():
 if len(number) != 10:
  print("phone number must contain 10 digits\n")
 else: 
  number = int(number)
  if number in phonebook.keys():
   print(phonebook.get(number)[0][0], phonebook.get(number)[0][1], "from", phonebook.get(number)[1][0]+",", phonebook.get(number)[1][1])
  else:
   print("the number was not found\n")
else:
 print("phone number must contain only digits\n")

