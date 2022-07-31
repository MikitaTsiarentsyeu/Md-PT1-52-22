import datetime
choice = input("Введние 1, если хотите вывести текущее время и 2, если ввести вручную:\n")
if choice != "1" and choice != "2":
    print("Неверный ввод")
elif choice == "1":
    dt_now = datetime.datetime.now()
    print("Текущее время:", dt_now.strftime("%H:%M"))
else:
    dt_input = input("Введите время(формат hh:mm):\n")
    if len(dt_input) != 5 or dt_input[2] != ':':
        print("Проверьте количество введенных цифр, cимвол ':' является обязательным")
    else:
        dt = dt_input.split(":")
        dt_input[2] == ":"
        hour = dt[0] 
        min = dt[1]
        if not (hour.isdigit() and min.isdigit()):
            print("Необходимо вводить только цифры в часах и минутах")
        hour, min = int(hour), int(min)
        if len(dt[0]) != 2 or len(dt[1]) != 2 or hour > 24 or min > 59: 
            print("Введен неверный формат данных, проверьте корректность ввода времени")
        d1_hour = {0:'двенадцать',1:'час',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',11:'одиннадцать'}
        d2_hour = {0:'первого',1:'второго',2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 10:'одиннадцатого', 11 :'двеннадцатого'}
        d3_min = {11:'одиннадцать',12:'двенадцать',13:'тринадцать',14:'четырнадцать',15:'пятнадцать',16:'шестнадцать',17:'семнадцать',18:'восемнадцать',19:'девятнадцать',0:'ровно',10:'десять',30:'половина'}
        d4_min = {45:'пятнадцати',46:'четырнадцати', 47:'тринадцати', 48:'двенадцати', 49:'одиннадцати', 50:'десяти', 51:'девяти', 52:'восьми', 53:'семи', 54:'шести', 55:'пяти', 56:'четырех', 57:'трех', 58:'двух', 59:'одной'}
        d5_min_full = {20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят'} 
        d6_min_last = {1:'одна',2:'две',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
        if hour > 11:
            hour -= 12
        if min == 0:
            if hour > 4 or hour == 0:
                connect = ' часов '
                output = f'{d1_hour[hour]}{connect}'
            else:
                connect = ' час ' if hour == 1 else ' часа '
            output = f'{d1_hour[hour]}{connect}{d3_min[min]}'
        elif min == 30:
            output = f'{d3_min[min]} {d2_hour[hour]}'    
        elif min >= 45:
            output = f'без {d4_min[min]} минут {d1_hour[0]}' if hour == 11 else f'без {d4_min[min]} минут {d1_hour[hour+1]}'
            if min == 59:
                output = output.replace('минут','минуты')
        else:
            if min in d3_min:
                output = f'{d3_min[min]} минут {d2_hour[hour]}' 
            elif min % 10 == 0:
                output = f'{d5_min_full[min]} минут {d2_hour[hour]}' 
            else:
                last_number_minutes = min % 10
                first_number_minutes = min - last_number_minutes  
                output = f'{d6_min_last[last_number_minutes]} минут {d2_hour[hour]}' if first_number_minutes == 0 else f'{d5_min_full[first_number_minutes]} {d6_min_last[last_number_minutes]} минут {d2_hour[hour]}' 
                if last_number_minutes < 5:
                    output = output.replace('минут','минута') if last_number_minutes == 1 else  output.replace('минут','минуты')
        print(output)  
    