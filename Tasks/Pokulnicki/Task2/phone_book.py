database_of_numbers = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("-=====The program to find a person by phone number=====-")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

search_number = input("Please, enter the phone number.\
 The number should consist of only ten numbers. Make your entry:\n")

len_keys_database = len(str(list(database_of_numbers.keys())[0])) # determine the length of the key

while True:
    if search_number.isnumeric():
        if  len_keys_database == len(search_number) and int(search_number) in database_of_numbers:
            search_result = database_of_numbers.get(int(search_number),"the number was not found")
            name = search_result[0][0]
            last_name = search_result[0][1]
            city = search_result[1][0]
            state = search_result[1][1]
            print("{{{}}} {{{}}} from {{{}}}, {{{}}}".format(name,last_name,city,state))
            break
        elif len_keys_database == len(search_number):
            search_result = database_of_numbers.get(int(search_number),"the number was not found")
            print(search_result)
            break
        else:
            print ("Incorrect input (the number of digits should be ten). Please, make the correct entry.\n")
        search_number = input("Please, enter the phone number.\
 The number should consist of only ten numbers. Make your entry:\n")
        continue
    else:
        print ("Incorrect input (the phone number should be consist only of numbers.) Please, make the correct entry.\n")
        search_number = input("Please, enter the phone number.\
 The number should consist of only ten numbers. Make your entry:\n")
        continue
        
    


