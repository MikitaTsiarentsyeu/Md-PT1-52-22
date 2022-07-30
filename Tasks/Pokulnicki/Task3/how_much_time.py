import datetime as dt
from datetime import datetime

name_of_hours = {1 : "один", 2 : "два", 3 : "три",
                 4 : "четыре", 5 : "пять", 6 : "шесть",
                 7 : "семь", 8 : "восемь", 9 : "девять",
                 10 : "десять", 11 : "одиннадцать", 
                 12 : "двенадцать", 13 : "один"}

name_of_hours_ordinal = {1 : "первого", 2 : "второго", 3 : "третьего",
                         4 : "четвертого", 5 : "пятого", 6 : "шестого",
                         7 : "седьмого", 8 : "восьмого", 9 : "девятого",
                         10 : "десятого", 11 : "одиннадцатого", 12 : "двенадцатого",
                         13 : "первого"}

name_of_minute_upto30 = {1 : "одна", 2 : "две", 3 : "три",
                         4 : "четыре", 5 : "пять", 6 : "шесть",
                         7 : "семь", 8 : "восемь", 9 : "девять",
                         10 : "десять", 11 : "одиннадцать", 12 : "двенадцать",
                         13 : "тринадцать", 14 : "четырнадцать", 15 : "пятнадцать",
                         16 : "шестнадцать", 17 : "семнадцать", 18 : "восемнадцать",
                         19 : "девятнадцать", 20 : "двадцать", 21 : "двадцать одна",
                         22 : "двадцать две", 23 : "двадцать три", 24 : "двадцать четыре",
                         25 : "двадцать пять", 26 : "двадцать шесть", 27 : "двадцать семь",
                         28 : "двадцать восемь", 29 : "двадцать девять"}

name_of_minute_after30 = {31 : "тридцать одна", 32 : "тридцать две", 33 : "тридцать три",
                          34 : "тридцать четыре", 35 : "тридцать пять", 36 : "тридцать шесть",
                          37 : "тридцать семь", 38 : "тридцать восемь",39 : "тридцать девять",
                          40 : "сорок", 41 : "сорок одна", 42 : "сорок две",
                          43 : "сорок три", 44 : "сорок четыре"}

name_of_minute_after45 = {1 : "одной", 2 : "двух", 3 : "трех",
                          4 : "четырех", 5 : "пяти", 6 : "шести",
                          7 : "семи", 8 : "восьми", 9 : "девяти",
                          10 : "десяти", 11 : "одиннадцати", 12 : "двенадцати",
                          13 : "тринадцати", 14 : "четырнадцати", 15 : "пятнадцати"}

current_hours = 0
current_minute = 0
current_time_format = 0
print("-========================= Программа часы =========================- ")

#validation part 
while True:
    choise = input("Выберите способ ввода текущего времени, пожалуйста. Использовать системное время --> 0, ввод из консоли --> 1, сделайте свой выбор:\n")
    if choise.isnumeric():
        if int(choise) == 0:
            x = dt.datetime.now()
            current_time_format = x.strftime('%H:%M')
            current_hours = x.hour
            current_minute = x.minute
            break
        elif int(choise) == 1:
            while True:
                input_time = input("Введите время в формате hh:mm (00:00 - 23:59):\n")
                if len(input_time) == len(str("hh:mm")) and input_time.find(":") != -1 and input_time.replace(":","").isnumeric():
                    if 0 <= int(input_time[0:2]) < 24 and 0 <= int(input_time[3:5]) <= 60:
                        x = datetime.strptime(input_time,"%H:%M")
                        current_time_format = x.strftime('%H:%M')
                        current_hours = x.hour
                        current_minute = x.minute
                        break
                    else:
                        print ("Неверный формат времени, повторите попытку hh:mm (00:00 - 23:59)")
                        continue
                else:
                    print ("Неверный ввод, пожалуйста соблюдайте формат ввода hh:mm (00:00 - 23:59)")
                    continue
            break
        else:
            print("Неверный ввод, введите 0 или 1, сделайте свой выбор")   
    else: 
        print("Неверный ввод, введите 0 или 1, сделайте свой выбор") 

      
if current_hours > 12:
    current_hours = current_hours - 12
elif current_hours == 0:
    current_hours = 12

#condition min == 0
if current_minute == 0 and 1 < current_hours < 5:
    print(f"({current_time_format} - {name_of_hours[current_hours]} часа ровно)")
elif current_minute == 0 and current_hours >= 5:
    print(f"({current_time_format} - {name_of_hours[current_hours]} часов ровно)")
elif current_minute == 0 and current_hours == 1:
    print(f"({current_time_format} - {name_of_hours[current_hours]} час ровно)")

#condition min == 30
if current_minute == 30 and current_hours != 12:
    print(f"({current_time_format} - половина {name_of_hours_ordinal[current_hours+1]})")
elif current_minute == 30 and current_hours == 12:
    print(f"({current_time_format} - половина {name_of_hours_ordinal[current_hours-11]})")

#condition min < 30
if current_minute == 1 or current_minute == 21:
    print(f"({current_time_format} - {name_of_minute_upto30[current_minute]} минута {name_of_hours_ordinal[current_hours+1]})")
elif 1 < current_minute < 5 or 21 < current_minute < 25:
    print(f"({current_time_format} - {name_of_minute_upto30[current_minute]} минуты {name_of_hours_ordinal[current_hours+1]})")
elif 4 < current_minute < 21 or 24 < current_minute <= 29 :
    print(f"({current_time_format} - {name_of_minute_upto30[current_minute]} минут {name_of_hours_ordinal[current_hours+1]})")

#min > 30 and min < 45
if current_minute == 31 or current_minute == 41:
    print(f"({current_time_format} - {name_of_minute_after30[current_minute]} минута {name_of_hours_ordinal[current_hours+1]})")
elif 31 < current_minute < 35 or 41 < current_minute <= 44:
    print(f"({current_time_format} - {name_of_minute_after30[current_minute]} минуты {name_of_hours_ordinal[current_hours+1]})")
elif 34 < current_minute < 41:
    print(f"({current_time_format} - {name_of_minute_after30[current_minute]} минут {name_of_hours_ordinal[current_hours+1]})")

#min >= 45
if current_minute == 59:
    print(f"({current_time_format} - без {name_of_minute_after45[60 - current_minute]} минуты {name_of_hours[current_hours+1]})")
elif 45 <= current_minute < 60: 
    print(f"({current_time_format} - без {name_of_minute_after45[60 - current_minute]} минут {name_of_hours[current_hours+1]})")
