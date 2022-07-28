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