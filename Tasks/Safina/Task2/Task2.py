dict = {9103976271:[("Rehina", "Meinhard"),("Memphos", "Tennessee")],
4199392609:[("Stephonie", "Bruse"),("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takya"),("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number = input("\nPlease, enter the phone number:\n")

if number.isdigit():
   if len(number) > 10:
      print("Error:You entered too long a number")
   elif len(number) < 10:
      print("Error:You entered too short a number")
        
   else:  
      number = int(number)
      if number in dict.keys ():
         print(f"{{{dict.get(number)[0][0]}}} {{{dict.get(number)[0][1]}}} from {{{dict.get(number)[1][0]}}}, {{{dict.get(number)[1][1]}}}")
      else:
         print("The number was not found")

else:
    print("Please, enter the correct number")   
    
          


   







  









    





