from ctypes import addressof
import sys


phonebook = {
    9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]
}
search_phone = input("Please provide phone number:")

#  Solution 1: if-in

if (search_phone.isdigit()) == False or len(search_phone) != 10:
    print ("Phone number is invalid, please check and try again.")
elif int(search_phone) in phonebook:
    phone_number = int(search_phone)
    print(f"{phonebook[phone_number][0][0]} {phonebook[phone_number][0][1]} from {phonebook[phone_number][1][0]}, {phonebook[phone_number][1][1]}")
else:
    print("the number was not found")

#  Solution 2: for-in loop (very bad solution, just for learning purposes)

if (search_phone.isdigit()) == False or len(search_phone) != 10:
        sys.exit("Phone number is invalid, please check and try again.")

for key, value in phonebook.items():
    if int(search_phone) == key:
        print(f"{value[0][0]} {value[0][1]} from {value[1][0]}, {value[1][1]}")
        sys.exit()
print("the number was not found")



