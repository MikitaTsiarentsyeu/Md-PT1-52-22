# Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого с консоли (hh:mm).
# (дать пользователю возможность выбрать режим работы программы)

# Для получения текущего времени использовать модуль datetime.

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)


import datetime


number_list_0_59 =  ["ноль", "один","два","три","четыре","пять","шесть","семь","восемь","девять", "десять", "одиннадцать", "двенадцать", 
                     "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать",
                     "двадцать один", "двадцать два", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь",
                     "двадцать восемь", "двадцать девять", "тридцать", "тридцать один", "тридцать два", "тридцать три", "тридцать четыре", 
                     "тридцать пять", "тридцать шесть", "тридцать семь", "тридцать восемь", "тридцать девять","сорок", "сорок один", 
                     "сорок два", "сорок три", "сорок четыре", "сорок пять", "сорок шесть", "сорок семь", "сорок восемь", "сорок девять", 
                     "пятьдесят", "пятьдесят один", "пятьдесят два", "пятьдесят три", "пятьдесят четыре", "пятьдесят пять", "пятьдесят шесть",
                     "пятьдесят семь", "пятьдесят восемь", "пятьдесят девять"]
number_list_chisl = ["первого", "второго", "третьего", "четвёртого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", 
                     "одиннадцатого", "двенадцатого"]
number_list_bez   = ["одной", "двух", "трёх", "четырёх", "пяти", "шести", "семи", "восьми", "девяти", "десяти", "одиннадцати", "двенадцати",
                     "тринадцати", "четырнадцати", "пятнадцати"]
number_list_2     = ["ноль", "одна", "две", "три","четыре","пять","шесть","семь","восемь","девять", "десять", "одиннадцать", "двенадцать", 
                     "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", 
                     "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь",
                     "двадцать восемь", "двадцать девять", "тридцать", "тридцать одна", "тридцать две", "тридцать три", "тридцать четыре", 
                     "тридцать пять", "тридцать шесть", "тридцать семь", "тридцать восемь", "тридцать девять","сорок", "сорок одна", "сорок две",
                     "сорок три", "сорок четыре", "сорок пять", "сорок шесть", "сорок семь", "сорок восемь", "сорок девять"]
while True:
    enter_time = input ('Выберите режим работы программы:\n 1 - текстовый вывод текущего времени \n 2 - текстовый вывод времени, введённого с консоли (hh:mm) \n')

    if (enter_time == '1'):
        dt_obj =datetime.datetime.now()
        dt_string = dt_obj.strftime("%H:%M")
        dt_string = list(dt_string)
        dt_string_1 = dt_string [0:2]
        dt_string_2 = dt_string [3:]
        dt_string_3 = dt_string_1 + dt_string_2
        hh = dt_string_3[0] + dt_string_3[1]
        mm = dt_string_3[2] + dt_string_3[3]
        print (hh,":",mm)
        hh = int(hh)
        mm = int(mm)

        if mm == 0:        
            if hh == 1:
                print (number_list_0_59[hh].capitalize(), 'час ровно')
            elif hh == 13:
                print (number_list_0_59[hh-12].capitalize(), 'час ровно')
            elif hh >= 2 and hh <= 4:
                print (number_list_0_59[hh].capitalize(), 'часа ровно')
            elif hh >= 14 and hh <= 16:
                print (number_list_0_59[hh-12].capitalize(), 'часа ровно')
            elif hh >= 17 and hh <= 23:
                print (number_list_0_59[hh-12].capitalize(), 'часов ровно')
            else: 
                print (number_list_0_59[hh].capitalize(), 'часов ровно')

        elif mm > 0 and mm < 30:       
            if mm == 1 or mm == 21:
                if hh >= 12 and hh <= 23:
                    print (number_list_2[mm].capitalize(), "минута", number_list_chisl[hh-12])
                else:
                    print (number_list_2[mm].capitalize(), "минута", number_list_chisl[hh])
            elif mm == 2 or mm == 22:
                if hh >= 12 and hh <= 23:
                    print (number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print (number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh])
            elif mm >= 3 and mm <= 4 or mm >= 23 and mm <= 24:
                if hh >= 12 and hh <= 23:
                    print (number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print (number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh])
            else:
                if hh >= 12 and hh <= 23:
                    print (number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh-12])
                else:
                    print (number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh])

        elif mm == 30:
            if hh >= 0 and hh <= 11:
                print("Половина", number_list_chisl[hh])
            else:
                hh >= 12 and hh <= 23
                print("Половина", number_list_chisl[hh-12])

        elif mm > 30 and mm < 45:
            if mm == 31 or mm == 41:
                if  hh >= 12 and hh <= 23:
                    print(number_list_2[mm].capitalize(), "минута", number_list_chisl[hh-12])
                else:
                    print(number_list_2[mm].capitalize(), "минута", number_list_chisl[hh])
            elif mm == 32 or mm == 42:
                if  hh >= 12 and hh <= 23:
                    print(number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print(number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh])
            elif mm >= 33 and mm <= 34 or mm >= 43 and mm <= 44:
                if  hh >= 12 and hh <= 23:
                    print(number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print(number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh])
            else:
                if  hh >= 12 and hh <= 23:
                    print(number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh-12])
                else:
                    print(number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh])
            
        elif mm >= 45:
            if hh >= 0 and hh <= 11:
                if mm == 59:
                    print ("Без",  number_list_bez[59-mm], "минуты",  number_list_0_59[hh+1])
                else:
                    print("Без",  number_list_bez[59-mm], "минут",  number_list_0_59[hh+1])
            else:
                if  hh >= 12 and hh <= 23:
                    if mm == 59:
                        print ("Без",  number_list_bez[59-mm], "минуты",  number_list_0_59[hh-11])
                    else:
                        print("Без",  number_list_bez[59-mm], "минут",  number_list_0_59[hh-11])
    
    elif (enter_time == '2'):

        while True :
            hh = int(input('Введите время, часы (00-23):\n'))
            if  hh >= 0 and hh <= 23:                
                break
            else:
                print ("Некорректный ввод. Диапазон должен быть от 0 до 23")
            
            
        while True :
            mm = int(input('Введите время, минуты (00-59):\n'))
            if  mm >= 0 and mm <= 59:                
                break
            else:
                print ("Некорректный ввод. Диапазон должен быть от 0 до 59")

        print(f'{hh:02}:{mm:02}')

        if mm == 0:        
            if hh == 1:
                print (number_list_0_59[hh].capitalize(), 'час ровно')
            elif hh == 13:
                print (number_list_0_59[hh-12].capitalize(), 'час ровно')
            elif hh >= 2 and hh <= 4:
                print (number_list_0_59[hh].capitalize(), 'часа ровно')
            elif hh >= 14 and hh <= 16:
                print (number_list_0_59[hh-12].capitalize(), 'часа ровно')
            elif hh >= 17 and hh <= 23:
                print (number_list_0_59[hh-12].capitalize(), 'часов ровно')
            else: 
                print (number_list_0_59[hh].capitalize(), 'часов ровно')

        elif mm > 0 and mm < 30:       
            if mm == 1 or mm == 21:
                if hh >= 12 and hh <= 23:
                    print (number_list_2[mm].capitalize(), "минута", number_list_chisl[hh-12])
                else:
                    print (number_list_2[mm].capitalize(), "минута", number_list_chisl[hh])
            elif mm == 2 or mm == 22:
                if hh >= 12 and hh <= 23:
                    print (number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print (number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh])
            elif mm >= 3 and mm <= 4 or mm >= 23 and mm <= 24:
                if hh >= 12 and hh <= 23:
                    print (number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print (number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh])
            else:
                if hh >= 12 and hh <= 23:
                    print (number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh-12])
                else:
                    print (number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh])

        elif mm == 30:
            if hh >= 0 and hh <= 11:
                print("Половина", number_list_chisl[hh])
            else:
                hh >= 12 and hh <= 23
                print("Половина", number_list_chisl[hh-12])

        elif mm > 30 and mm < 45:
            if mm == 31 or mm == 41:
                if  hh >= 12 and hh <= 23:
                    print(number_list_2[mm].capitalize(), "минута", number_list_chisl[hh-12])
                else:
                    print(number_list_2[mm].capitalize(), "минута", number_list_chisl[hh])
            elif mm == 32 or mm == 42:
                if  hh >= 12 and hh <= 23:
                    print(number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print(number_list_2[mm].capitalize(), "минуты", number_list_chisl[hh])
            elif mm >= 33 and mm <= 34 or mm >= 43 and mm <= 44:
                if  hh >= 12 and hh <= 23:
                    print(number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh-12])
                else:
                    print(number_list_0_59[mm].capitalize(), "минуты", number_list_chisl[hh])
            else:
                if  hh >= 12 and hh <= 23:
                    print(number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh-12])
                else:
                    print(number_list_0_59[mm].capitalize(), "минут", number_list_chisl[hh])
            
        elif mm >= 45:
            if hh >= 0 and hh <= 11:
                if mm == 59:
                    print ("Без",  number_list_bez[59-mm], "минуты",  number_list_0_59[hh+1])
                else:
                    print("Без",  number_list_bez[59-mm], "минут",  number_list_0_59[hh+1])
            else:
                if  hh >= 12 and hh <= 23:
                    if mm == 59:
                        print ("Без",  number_list_bez[59-mm], "минуты",  number_list_0_59[hh-11])
                    else:
                        print("Без",  number_list_bez[59-mm], "минут",  number_list_0_59[hh-11])
        
    else:
        print ('Неправильный ввод')
        break