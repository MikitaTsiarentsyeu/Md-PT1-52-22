from datetime import datetime

d_min = { 0: "ноль", 1: "одна",2: "две",3: "три", 4:"четыре",5: "пять", 6: "шесть",7: "семь",8: "восемь",9: "девять",10: "десять",11:  "одиннадцать",12: "двенадцать", 
                     13: "тринадцать",14: "четырнадцать",15: "пятнадцать",16: "шестнадцать", 17: "семнадцать",18:  "восемнадцать", 19:"девятнадцать",20: "двадцать",
                     21:"двадцать одна", 22:"двадцать две",23:  "двадцать три",24:  "двадцать четыре",25: "двадцать пять",26: "двадцать шесть",27: "двадцать семь",
                     28:"двадцать восемь", 29: "двадцать девять",30: "тридцать", 31:"тридцать одна",32: "тридцать две",33: "тридцать три",34: "тридцать четыре", 
                     35:"тридцать пять",36: "тридцать шесть",37: "тридцать семь", 38:"тридцать восемь",39: "тридцать девять",40:"сорок", 41:"сорок одна", 
                     42:"сорок две", 43:"сорок три",44: "сорок четыре",45: "сорок пять", 46:"сорок шесть",47: "сорок семь",48: "сорок восемь",49: "сорок девять", 
                     50:"пятьдесят", 51: "пятьдесят одна", 52:"пятьдесят две",53: "пятьдесят три", 54:"пятьдесят четыре",55: "пятьдесят пять",56: "пятьдесят шесть",
                     57:"пятьдесят семь", 58:"пятьдесят восемь",59: "пятьдесят девять"}                     

d_hours = { 0: "двенадцать", 1: "один",2: "два",3: "три", 4:"четыре",5: "пять", 6: "шесть",7: "семь",8: "восемь",9: "девять",10: "десять",11:  "одиннадцать",12: "двенадцать", 
                     13: "один",14: "два",15: "три",16: "четыре", 17: "пять",18:  "шесть", 19:"семь",20: "восемь",
                     21:"девять", 22:"десять",23:  "одиннадцать",24:  "двенадцать",}
d_bez =  {45: "пятнадцати", 46:"четырнадцати",47: "тринадцати",48: "двенадцати",49: "одиннадцати", 
                     50:"десяти", 51: "девяти", 52:"восьми",53: "семи", 54:"шести",55: "пяти",56: "четырех",
                     57:"трех", 58:"двух",59: "одной"}   

d_half = {0: "первого", 1: "второго",2: "третьего",3: "четвертого", 4:"пятого",5: "шестого", 6: "седьмого",7: "восьмого",8: "девятого",9: "десятого",10: "одиннадцатого",11:  "двенадцатого",12: "первого", 
                     13: "второго",14: "третьего",15: "четвертого",16: "пятого", 17: "шестого",18:  "седьмого", 19:"восьмого",20: "девятого",
                     21:"десятого", 22:"одиннадцатого",23:"двенадцатого"}   



date_input = input("""Пожалуйста, выберите действие:
    1.Текстовый вывод текущего времени.
    2.Текстовый вывод времени, введённого с консоли (hh:mm).
    """)   
minutes, hours = 0, 0

if date_input == ('1'):
    current_date = datetime.now().time()
    minutes = current_date.minute
    hours = current_date.hour

elif date_input == ('2'):
    while True:
        time_input = input("Пожалуйста, введите время в  hh:mm формате:\n")

        if len(time_input) != 5:
            print("Неправильная длина строки времени")
            continue

        if time_input[2] != ":":
            print("Неправильный ввод, утерян : символ")
            continue

        values = time_input.split(':')
        hours, minutes = values[0], values[1]

        if not (hours.isdigit() and minutes.isdigit()):
            print("Неправильный ввод, вводимые часы и минуты должны быть цифрами")
            continue

        hours, minutes = int(hours), int(minutes)

        if hours > 24 or minutes > 59:
            print("Неправиьный ввод, часы должны варьироватья от  00 до 24, а минуты от  00 до 59")
            continue

        break

if minutes == 00:
    if hours == 0:
        print(f"{d_hours.get(hours)} часов ровно")
    elif hours == 1 and hours == 13:
        print(f"{d_hours.get(hours)} час ровно")
    elif  hours >= 2 and hours <= 4 :
        print(f"{d_hours.get(hours)} часа ровно")
    elif hours >= 14 and hours <= 16:
        print(f"{d_hours.get(hours)} часа ровно")  
    elif  hours >= 5 and hours <= 12:
        print(f"{d_hours.get(hours)} часов ровно")
    elif  hours >= 17 and hours <= 24:
        print(f"{d_hours.get(hours)} часов ровно") 

if minutes >= 1 and minutes <= 29:
    if minutes == 1 and minutes == 21:
            print(f"{d_min.get(minutes)} минута {d_half.get(hours)}")
    elif minutes >= 2 and minutes <= 4:
        print(f"{d_min.get(minutes)} минуты {d_half.get(hours)}") 
    elif minutes >= 5 and minutes <= 20:
        print(f"{d_min.get(minutes)} минут {d_half.get(hours)}")
    elif minutes >= 22 and minutes <= 24:
        print(f"{d_min.get(minutes)} минуты {d_half.get(hours)}") 
    elif minutes >= 25 and minutes <= 29:
        print(f"{d_min.get(minutes)} минут {d_half.get(hours)}")     

if minutes == 30:
    print(f" половина {d_half.get(hours)}")    

if minutes > 30 and minutes < 45:
    if minutes == 31 and minutes == 41:
        print(f"{d_min.get(minutes)} минута {d_half.get(hours)}")  
    elif minutes >= 32 and minutes < 34:
        print(f"{d_min.get(minutes)} минуты {d_half.get(hours)}")
    elif minutes >= 35 and minutes < 40:
        print(f"{d_min.get(minutes)} минут {d_half.get(hours)}")
    elif minutes >= 42 and minutes < 44:
        print(f"{d_min.get(minutes)} минуты {d_half.get(hours)}")             

if minutes >= 45:
    print(f"без {d_bez.get(minutes)} минут {d_hours.get(hours+1)}")    