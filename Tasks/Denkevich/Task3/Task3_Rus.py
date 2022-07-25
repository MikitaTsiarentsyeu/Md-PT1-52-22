import datetime

d = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
     7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
     13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
     18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 21: 'двадцать один', 22: 'двадцать два',
     23: 'двадцать три', 24: 'двадцать четыре', 25: 'двадцать пять', 26: 'двадцать шесть', 27: 'двадцать семь', 28: 'двадцать восемь',
     29: 'двадцать девять', 30: 'тридцать', 31: 'тридцать один', 32: 'тридцать two', 33: 'тридцать three', 34: 'тридцать четыре',
     35: 'тридцать пять', 36: 'тридцать шесть', 37: 'тридцать семь', 38: 'тридцать восемь', 39: 'тридцать девять', 40: 'сорок',
     41: 'сорок один', 42: 'сорок два', 43: 'сорок three', 44: 'сорок четыре', 45: 'сорок пять', 46: 'сорок шесть',
     47: 'сорок семь', 48: 'сорок восемь', 49: 'сорок девять', 50: 'пятьдесят', 51: 'пятьдесят один', 52: 'пятьдесят two',
     53: 'пятьдесят three', 54: 'пятьдесят четыре', 55: 'пятьдесят пять', 56: 'пятьдесят шесть', 57: 'пятьдесят семь', 58: 'пятьдесят восемь',
     59: 'пятьдесят девять', 60: 'шестьдесят'}
d1 = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвёртого', 5: 'пятого', 6: 'шестого', 7: 'седьмого', 8: 'восьмого',
      9: 'девятого', 10: 'десятого', 11: 'одинадцатого', 12: 'двенадцатого'}
d2 = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре'}
d3 = {1: 'одной', 2: 'двух', 3: 'трёх', 4: 'четырёх', 5: 'пяти', 6: 'шести', 7: 'семи', 8: 'восьми', 9: 'девяти',
      10: 'десяти', 11: 'одинадцати', 12: 'двенадцати', 13: 'тринадцати', 14: 'четырнадцати', 15: 'пятнадцати'}

n = 0
while True:
    n += 1
    inp = input(
        '\n-------------------\nЕсли хотите узнать текущее время, введите 1.\nЕсли хотите ввести своё время, введите 2.\nДля выхода нажмите 3.\n')
    currentTime = datetime.datetime.today().strftime('%H:%M')
    if inp == '1':
        time = currentTime
    elif inp == '2':
        userTime = input('Пожалуйста, введите время в формате HH:MM:\n')
        time = userTime
    elif inp == '3':
        exit()
    else:
        print('Неправильный ввод. Попробуйте ещё раз.')
        if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
            print(f'   БортЖурнал: программа отработала {n} раза')
        else:
            print(f'   БортЖурнал: программа отработала {n} раз')
        continue
    if len(time) != 5 or time[0:2].isdigit() == False or time[2] != ':' or time[3:5].isdigit() == False:
        print('Неправильный ввод времени. Попробуйте ещё раз.')
        if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
            print(f'   БортЖурнал: программа отработала {n} раза')
        else:
            print(f'   БортЖурнал: программа отработала {n} раз')
        continue
    elif int(time[0:2]) == 24 and int(time[3:5]) == 60:
        print("""
        ****  *  *       ****  ****
           *  *  *   *   *     *  *
           *  *  *   *   *     *  *
        ****  ****       ****  *  *
        *        *   *   *  *  *  *
        *        *   *   *  *  *  *
        ****     *       ****  ****
        """)
    elif int(time[0:2]) > 23 or int(time[3:5]) >= 60:
        print('Неправильный ввод времени. Попробуйте ещё раз.')
        if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
            print(f'   БортЖурнал: программа отработала {n} раза')
        else:
            print(f'   БортЖурнал: программа отработала {n} раз')
        continue
    else:
        h = int(time[0:2])
        m = int(time[3:5])
        h1 = int(time[0:2][-1])
        m1 = int(time[3:5][-1])

        if m == 0:
            if h <= 12:
                if h == 1:
                    print(f'{d[h][0:1].upper()}{d[h][1:]} час ровно.')
                    if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
                        print(f'   БортЖурнал: программа отработала {n} раза')
                    else:
                        print(f'   БортЖурнал: программа отработала {n} раз')
                    continue
                elif (h >= 5 and h <= 20):
                    print(f'{d[h][0:1].upper()}{d[h][1:]} часов ровно.')
                elif h == 0:
                    print(f'{d[h+12][0:1].upper()}{d[h+12][1:]} часов ровно.')
                else:
                    print(f'{d[h][0:1].upper()}{d[h][1:]} часа ровно.')
            elif h > 12:
                h = h - 12
                if h == 1:
                    print(f'{d[h][0:1].upper()}{d[h][1:]} час ровно.')
                    if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
                        print(f'   БортЖурнал: программа отработала {n} раза')
                    else:
                        print(f'   БортЖурнал: программа отработала {n} раз')
                    continue
                elif h >= 5 and h <= 20:
                    print(f'{d[h][0:1].upper()}{d[h][1:]} часов ровно.')
                else:
                    print(f'{d[h][0:1].upper()}{d[h][1:]} часа ровно.')

        if m < 30 or (m > 30 and m < 45):
            if h < 12:
                h = h + 1
                if m == 1 or m == 21 or m == 31 or m == 41:
                    if m == 1:
                        print(f'{d2[m][0].upper()}{d2[m][1:]} минута {d1[h]}.')
                    else:
                        print(f'{d[(int(str(m)[0]))*10][0].upper()}{d[(int(str(m)[0]))*10][1:]} {d2[int(str(m)[1])]} минута {d1[h]}')
                elif m >= 2 and m <= 4:
                    print(f'{d2[m][0].upper()}{d2[m][1:]} минуты {d1[h]}.')
                elif (m >= 22 and m <= 24) or (m >= 32 and m <= 34) or (m >= 42 and m <= 44):
                    print(
                        f'{d[int(str(m)[0])*10][0].upper()}{d[int(str(m)[0])*10][1:]} {d2[int(str(m)[-1])]} минуты {d1[h]}.')
                elif (m >= 5 and m <= 20) or (m >= 25 and m <= 30) or (m >= 35 and m <= 40):
                    print(f'{d[m][0].upper()}{d[m][1:]} минут {d1[h]}.')
            elif h >= 12:
                h = h - 11
                if m == 1 or m == 21 or m == 31 or m == 41:
                    if m == 1:
                        print(f'{d2[m][0].upper()}{d2[m][1:]} минута {d1[h]}.')
                    else:
                        print(f'{d[(int(str(m)[0]))*10][0].upper()}{d[(int(str(m)[0]))*10][1:]} {d2[int(str(m)[1])]} минута {d1[h]}')
                elif m >= 2 and m <= 4:
                    print(f'{d2[m][0].upper()}{d2[m][1:]} минуты {d1[h]}.')
                elif (m >= 22 and m <= 24) or (m >= 32 and m <= 34) or (m >= 42 and m <= 44):
                    print(
                        f'{d[int(str(m)[0])*10][0].upper()}{d[int(str(m)[0])*10][1:]} {d2[int(str(m)[-1])]} минуты {d1[h]}.')
                elif (m >= 5 and m <= 20) or (m >= 25 and m <= 30) or (m >= 35 and m <= 40):
                    print(f'{d[m][0].upper()}{d[m][1:]} минут {d1[h]}.')

        if m == 30:
            if h < 12:
                h = h + 1
                print(f'Половина {d1[h]}')
            if h >= 12:
                h = h - 11
                print(f'Половина {d1[h]}')

        if m >= 45 and m <= 59:
            if h < 12:
                h = h + 1
                print(f'Без {d3[60 - m]} минут {d[h]}')
            elif h >= 12:
                h = h - 11
                print(f'Без {d3[60 - m]} минут {d[h]}')
                
    if str(n)[-1] == '2' or str(n)[-1] == '3' or str(n)[-1] =='4':            
        print(f'   БортЖурнал: программа отработала {n} раза')
    else:
        print(f'   БортЖурнал: программа отработала {n} раз')