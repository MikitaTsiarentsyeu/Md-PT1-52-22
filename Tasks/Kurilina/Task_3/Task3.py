from datetime import datetime

while True:
    greeting = input("Please select the operating mode of the program. if you want to see your time in text format, enter 'yes', if the current time - enter 'no'\n")
    if greeting != 'yes' and greeting != 'no':
        print("Please, check your input, enter 'yes' or 'no'")
    else:
        break    

if greeting == 'no':
    current_datetime = datetime.now()
    hours = current_datetime.hour
    minutes = current_datetime.minute


while greeting == 'yes':
    time_token = input("Please input the time if the hh:mm format:\n")

    if len(time_token) != 5:
        print("Incorrect length of the time string")
        continue

    if time_token[2] != ":":
        print("Incorrect input, the token lacks the : symbol")
        continue

    values = time_token.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("Incorrect input, the hours and minutes values should be digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print("Incorrect input, the hours should vary from 00 to 2 and the minutes should vary from 00 to 59")
        continue

    break


dict_minutes_except = {11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятнадцать',0:'ровно',10:'десять',30:'половина'}
dict_minutes_except1 = {45:'пятнадцати',46:'четырнадцати', 47:'тринадцати', 48:'двенадцати', 49:'одиннадцати', 50:'десяти', 51:'девяти', 52:'восьми', 53:'семи', 54:'шести', 55:'пяти', 56:'четырех', 57:'трех', 58:'двух', 59:'одной'}
dict_have_not_last_number_minutes = {20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят'} 
dict_have_last_number_minutes = {1:'одна',2:'две',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
dict_hours = {0:'первого',1:'второго',2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 10:'одиннадцатого', 11 :'двеннадцатого'}
dict_hours_except = {0:'двенадцать',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',11:'одиннадцать'}
if hours > 11:
    hours -= 12
if minutes == 0:
    if hours > 4 or hours == 0:
        connect = ' часов '
    else:
        connect = ' час ' if hours == 1 else ' часа '
    finally_string = f'{dict_hours_except[hours]}{connect}{dict_minutes_except[minutes]}'
elif minutes == 30:
    finally_string = f'{dict_minutes_except[minutes]} {dict_hours[hours]}'    
elif minutes >= 45:
    finally_string = f'без {dict_minutes_except1[minutes]} минут {dict_hours_except[0]}' if hours == 11 else f'без {dict_minutes_except1[minutes]} минут {dict_hours_except[hours+1]}'
    if minutes == 59:
        finally_string = finally_string.replace('минут','минуты')
else:
     if minutes in dict_minutes_except:
        finally_string = f'{dict_minutes_except[minutes]} минут {dict_hours[hours]}' 
     elif minutes % 10 == 0:
        finally_string = f'{dict_have_not_last_number_minutes[minutes]} минут {dict_hours[hours]}' 
     else:
        last_number_minutes = minutes % 10
        first_number_minutes = minutes - last_number_minutes  
        finally_string = f'{dict_have_last_number_minutes[last_number_minutes]} минут {dict_hours[hours]}' if first_number_minutes == 0 else f'{dict_have_not_last_number_minutes[first_number_minutes]} {dict_have_last_number_minutes[last_number_minutes]} минут {dict_hours[hours]}'
        if last_number_minutes < 5:
            finally_string = finally_string.replace('минут','минута') if last_number_minutes == 1 else finally_string.replace('минут','минуты')


print(finally_string)    



hours = {1: "один", 2: "два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двенадцать"}
  minutes = {1:"одна", 2:"две", 3:"три", 4:"четыре", 5: "пять", 6: "шесть", 7 : "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать",  13 : "тринадцать", 14 : "четырнадцать", 15 : "пятнадцать",
16 : "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19 : "девятнадцать", 20: "двадцать", 21: "двадцать одна", 22: "двадцать две", 23: "двадцать три", 24 : "двадцать четыре", 25 : "двадцать пять", 26 : "двадцать шесть", 27 : "двадцать семь",
28 : "двадцать восемь", 29 : "двадцать девять"}
  hours1 = {1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 8:"восьмого", 9:"девятого", 10:"десятого", 11:"одиннадцатого", 12:"двенадцатого"}
  minutes2 = {1:"одной", 2:"двух", 3:"трех", 4:"четырех", 5:"пяти", 6:"шести", 7:"семи", 8:"восьми", 9:"девяти", 10:"десяти", 11:"одинннадцати", 12:"двенадцати", 13:"тринадцати", 14:"четырнадцати", 15:"пятнадцати"}

if current_time > 12:
    current_hours == current_hours - 12
elif current_hours == 0:
    current_hours = 12

if current_minute == 0 and 1 < current_hours < 5:
    print(f'(Сейчас:{hours[hour]} часа ровно)')
elif current_minute == 0 and current__hours >=5:
    print(f'Сейчас:{hours[hour]} часов ровно')
elif current_minute == 0 and current_hours == 1:
    print(f'Сейчас:{hours[hour]} час ровно')

if current_minute == 30 and current_hours != 12:
    print(f'Сейчас:половина {hours1[current_hours+1]}') 
elif current_minute == 30 and current_hours == 12:
    print(f'Сейчас: половина{hours1[current_hours-11]}')   

if current_minute == 1 or current_minute == 21:
    print(f"Сейчас: name_of_minute_upto30[current_minute]} минута {name_of_hours_ordinal[current_hours+1]})")
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
