d ={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

num = input("Enter phone number to find a person:\n")

x = False
while x == False:          
    while not num.isdigit() or len(str(num)) != len(str(list(d)[0])):
        num = input('Invalid input. The phone number must contain 10 digits only. Please re-enter\n')
        continue
    else:
        while int(num) not in list(d):  
            num = input("the number was not found. Please re-enter\n")
            x = False
            break
        else:
            info = d.get(int(num))                                       
            print(f'"{info[0][0]} {info[0][1]} from {info[1][0]} {info[1][1]}"')  #"{имя} {фамилия} from {city}, {state}"            
            x = True