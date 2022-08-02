from datetime import datetime

minute_dict = { 0: "ноль", 1: "одна",2: "две",3: "три", 4:"четыре",5: "пять", 6: "шесть",7: "семь",8: "восемь",9: "девять",10: "десять",11:  "одиннадцать",12: "двенадцать", 
13: "тринадцать",14: "четырнадцать",15: "пятнадцать",16: "шестнадцать", 17: "семнадцать",18:  "восемнадцать", 19:"девятнадцать",20: "двадцать",
21:"двадцать одна", 22:"двадцать две",23:  "двадцать три",24:  "двадцать четыре",25: "двадцать пять",26: "двадцать шесть",27: "двадцать семь",
28:"двадцать восемь", 29: "двадцать девять",30: "тридцать", 31:"тридцать одна",32: "тридцать две",33: "тридцать три",34: "тридцать четыре", 
35:"тридцать пять",36: "тридцать шесть",37: "тридцать семь", 38:"тридцать восемь",39: "тридцать девять",40:"сорок", 41:"сорок одна", 
42:"сорок две", 43:"сорок три",44: "сорок четыре"}

hour_dict = { 0: "двенадцать", 1: "один",2: "два",3: "три", 4:"четыре",5: "пять", 6: "шесть",7: "семь",8: "восемь",9: "девять",10: "десять",11:  "одиннадцать",12: "двенадцать", 
13: "один",14: "два",15: "три",16: "четыре", 17: "пять",18:  "шесть", 19:"семь",20: "восемь",
21:"девять", 22:"десять",23:  "одиннадцать",24:  "двенадцать",}

ten_dict = {20:'двадцать',30:'тридцать',40:'сорок',50:'пятьдесят'} 

quarter_dict = {45: "пятнадцати", 46:"четырнадцати",47: "тринадцати",48: "двенадцати",49: "одиннадцати", 
50:"десяти", 51: "девяти", 52:"восьми",53: "семи", 54:"шести",55: "пяти",56: "четырех",
57:"трех", 58:"двух",59: "одной", 0: "ровно", 30: "половина"} 

half_dict = {0: "первого", 1: "второго",2: "третьего",3: "четвертого", 4:"пятого",5: "шестого", 6: "седьмого",7: "восьмого",8: "девятого",9: "десятого",10: "одиннадцатого",11:  "двенадцатого",12: "первого", 
13: "второго",14: "третьего",15: "четвертого",16: "пятого", 17: "шестого",18:  "седьмого", 19:"восьмого",20: "девятого",
21:"десятого", 22:"одиннадцатого",23:"двенадцатого"}

x = input ('Пожалуйста введите свое имя:\n')
print ('Здравствуйте,', x, end = '!\n')
time = input('Выберите номер, подходящего для вас варианта:\n 1. Вывод текущего времени\n 2. Ввод времени с консоли\n 3. Завершение работы\n')
if time == '1':
    now_time = datetime.now().time()
    minute = now_time.minute
    hour = now_time.hour
    print(now_time.strftime("%H:%M"))
elif time == '3':
    print('Понятно, хорошего вам дня!')
elif time == '2':
    now_time = str(input('Введите время в формате hh:mm\n'))
    if now_time[2] != ':' or len(now_time) != 5:
        print('Отсутствует символ ":" или неверная длина строки, попробуйте еще раз')
    else:
        n = now_time.split(':')
        hour = n[0]
        minute = n[1]
        if not (n[0].isdigit() and n[1].isdigit()):
            print("Ошибка: время должно содержать лишь цифры")
        hour = int(n[0]) 
        minute = int(n[1])  
        if hour > 24 or minute > 59:
            print("Ошибка: часы указываются в промежутке от 00 до 23, минуты от 00 до 59")
        else:
            if hour > 11:
                hour -= 12
            if minute == 0:
                if hour > 4 or hour == 0:
                    t = ' часов '
                else:
                    t = ' час ' if hour == 1 else ' часа '
                finally_string = f'{hour_dict[hour]}{t}{quarter_dict[minute]}'
            elif minute == 30:
                finally_string = f'{quarter_dict[minute]} {half_dict[hour]}'    
            elif 60 >= minute >= 45:
                finally_string = f'без {minute_dict[minute]} минут {hour_dict[0]}' if hour == 11 else f'без {minute_dict[minute]} минут {half_dict[hour+1]}'
            if minute == 59:
                finally_string = finally_string.replace('минут','минуты')
            else:
                if minute in minute_dict:
                    finally_string = f'{minute_dict[minute]} минут {half_dict[hour]}' 
                elif minute % 10 == 0:
                    finally_string = f'{ten_dict[minute]} минут {half_dict[hour]}' 
                else:
                    last_number_minutes = minute % 10
                    first_number_minutes = minute - last_number_minutes  
                    finally_string = f'{minute_dict[last_number_minutes]} минут {half_dict[hour]}' if first_number_minutes == 0 else f'{ten_dict[first_number_minutes]} {quarter_dict[last_number_minutes]} минут {half_dict[hour]}'
                    if last_number_minutes < 5:
                        finally_string = finally_string.replace('минут','минута') if last_number_minutes == 1 else finally_string.replace('минут','минуты')

            print(finally_string)

    
        
         