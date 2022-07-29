d = {9103976271: [("Rehina", "Meinhard"), ("Memphos", "Tennessee")],
     4199392609: [("Stephonie", "Bruse"), ("Greensboro", "North Carolina")],
     9099459979: [("Ermes", "Angela"), ("Dallas", "Texas")],
     6123479367: [("Lorenza", "Takya"), ("Indianapolis", "Indiana")],
     7548993768: [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

n = input("\nEnter the phone number:\n")

if (n.isdigit()):
    if (len(n) > 10):
        print('To long number.')
    elif (len(n) < 10):
        print('To short number.')
    else:
        if (d.get(int(n)) != None):
            n = int(n)
            print(
                f"{d.get(n)[0][0]} {d.get(n)[0][1]} from {d.get(n)[1][0]}, {d.get(n)[1][1]}")
        else:
            print('The number was not found.')
else:
    print('Please enter only figures.')
