from datetime import datetime

while True:
    type = input("Введите 1 если хотите вывести текущее время и 2, если хотите ввести время вручную \n")
    if type != '1' and type != '2':
        print ('Ошибка.')
        continue
    elif type == '1':
        time_input = datetime.now()
        print ('Текущее время:', time_input.strftime("%H:%M"))
        hour = time_input.hour
        min = time_input.minute
    else:    
        time_input = input("Введите время в формате: hh:mm \n")
        if len(time_input) != 5:
            print("Введено неверное количество символов")
            continue
        if time_input[2] != ":":
            print("Ошибка. Не хватает символа ':'")
            continue
        time_split = (time_input.split(':'))
        hour = time_split[0]
        min = time_split[1]
        if not (hour.isdigit() and min.isdigit()):
            print("Ошибка. Должны быть введены только цифры")
            continue
        hour, min = int(hour), int(min)
        if hour > 24:
            print("Ошибка. Часы должны быть в диапазоне от 00 до 24")
            continue
        if min > 59:
            print("Ошибка. Минуты должны быть в диапазоне от 00 до 59")
            continue
        print(f'Вы ввели: {time_input}')
    break
min1 = min-min%10
min2 = min%10
if hour in range (13,24):
    hour -= 12
d1 = {1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять',10:'десять', 11:'одиннадцать', 12:'Двенадцать'}
d2 = {12:'первого', 1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 10:'одиннадцатого', 11:'двенадцатого'}
d3= {1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 19:'девятнадцать', 20:'двадцать', 30: 'тридцать', 40: 'сорок'}
d4 = {58: 'двух', 57: 'трех', 56: 'четырех', 55: 'пяти', 54: 'шести', 53: 'семи', 52: 'восьми', 51: 'девяти', 50: 'десяти', 49: 'одиннадцати', 48: 'двенадцати', 47: 'тринадцати', 46: 'четырнадцати', 45: 'пятнадцати'}
if min == 0:
    if hour == 1:
        print (f'Время: {d1[hour]} час ровно')
    elif hour in range (2,5):
        print (f'Время: {d1[hour]} часа ровно')
    else:
        print (f'Время: {d1[hour]} часов ровно')
elif min == 1:
    print (f'одна минута {d2[hour]}')
elif 2 < min < 5:
    print (f'Время: {d3[min]} минуты {d2[hour]}')
elif 5 < min < 21 or min == 40:
    print (f'Время: {d3[min]} минут {d2[hour]}')
elif min == 21 or min == 31 or min == 41:
    print (f'Время: {d3[min1]} {d3[min2]} минута {d2[hour]}')
elif 2 < min2 < 5 and min < 45:
    print (f'Время: {d3[min1]} {d3[min2]} минуты {d2[hour]}')
elif min == 30:
    print (f'Время: половина {d2[hour]}')
elif 25 < min < 45:
    print (f'Время: {d3[min1]} {d3[min2]} минут {d2[hour]}')
elif min == 59:
    if hour == 12:
       print ('Время: без одной минуты час')
    else:
       print (f'Время: без одной минуты {(d1[hour+1])}')
else:
    if hour == 12:
       print (f'Время: без {d4[min]} минут час')
    else:
       print (f'Время: без {d4[min]} минут {(d1[hour+1])}')