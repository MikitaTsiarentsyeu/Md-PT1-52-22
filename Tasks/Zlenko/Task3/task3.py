from datetime import datetime

rus_hours = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 0: "двенадцать"}
rus_minutes = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят"}
rus_hours_declensed = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого", 7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одиннадцатого", 12: "двенадцатого"}
rus_min_declensed = {1: "одной", 2: "двух", 3: "трех", 4: "четырех", 5: "пяти", 6: "шести", 7: "семи", 8: "восьми", 9: "девяти", 10: "десяти", 11: "одиннадцати", 12: "двенадцати", 13: "тринадцати", 14: "четырнадцати", 15: "пятнадцати"}

while True:
    timeMode = input("Please choose how you'd like to set the time: automatically or manually.\nType 'a' in case of auto-set or type 'm' in case of manual set: \n")
    if timeMode not in ('a', 'm'):
        print("Error: You've provided incorrect input. Please type exactly 'a' or 'm':\n")
    else:
        break

if timeMode == 'a':
    now = datetime.now()
    auto_time = now.strftime("%H:%M")
    hours, minutes = now.hour, now.minute
    time_printed = auto_time  # variable to print hh:mm time in final string
else:
    while True:
        manual_time = input("Please input the current time manually in hh:mm format: ")
        time_printed = manual_time # variable to print hh:mm time in final string
        if len(manual_time) != 5:
            print("Time format is incorrect. Please check the length (hh:mm).")
            continue
        if manual_time[2] != ":":
            print("Time format is incorrect. Please check the divider (hh:mm).")
            continue
        values = manual_time.split(":")
        hours, minutes = values[0], values[1]
        if not (hours.isdigit() and minutes.isdigit()):
            print("Invalid values provided. Expected digits.")
            continue   
        hours, minutes = int(hours), int(minutes)
        if hours > 24 or minutes > 59:
            print("Incorrect time provided. Hours should be in 00 - 24, and minutes in 00 - 59.")
        else:
            break
        
if hours > 11: # converting 1-24 time format to 1-12:
    hours -= 12

m = minutes%10 # splitting minutes into mm + m
mm = minutes-minutes%10

if minutes == 0:
    if hours == 1:
        print(f"{time_printed} - {rus_hours[hours]} час ровно")
    elif hours in range (2,5):
        print(f"{time_printed} - {rus_hours[hours]} часa ровно")
    else:
        print(f"{time_printed} - {rus_hours[hours]} часов ровно")

if minutes == 30:
        print(f"{time_printed} - половина {rus_hours_declensed[hours+1]}")    
 
if minutes in range (1, 21):
    if minutes == 1:
        print(f"{time_printed} - {rus_minutes[minutes]} минутa {rus_hours_declensed[hours+1]}")
    elif minutes in range (2, 5):
        print(f"{time_printed} - {rus_minutes[minutes]} минуты {rus_hours_declensed[hours+1]}") 
    else:
        print(f"{time_printed} - {rus_minutes[minutes]} минут {rus_hours_declensed[hours+1]}")

if minutes in range (21, 30) or minutes in range (31, 45):
    if m == 1:
        print(f"{time_printed} - {rus_minutes[mm]} {rus_minutes[m]} минута {rus_hours_declensed[hours+1]}")
    elif m in range (2, 5):
        print(f"{time_printed} - {rus_minutes[mm]} {rus_minutes[m]} минуты {rus_hours_declensed[hours+1]}")
    else: 
        print(f"{time_printed} - {rus_minutes[mm]} {rus_minutes[m]} минут {rus_hours_declensed[hours+1]}")

if minutes >= 45:
    if minutes == 59:
        print(f"{time_printed} - без {rus_min_declensed[60 - minutes]} минуты {rus_hours[hours+1]}")
    else:
       print(f"{time_printed} - без {rus_min_declensed[60 - minutes]} минут {rus_hours[hours+1]}")
