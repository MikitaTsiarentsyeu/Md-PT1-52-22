import datetime

hours_1 = {1:'Один час', 2:'Два часа', 3:'Три часа', 4:'Четыре часа', 5:'Пять часов', 6:'Шесть часов', 7:'Семь часов', 
           8:'Восемь часов', 9:'Девять часов', 10:'Десять часов', 11:'Одиннадцать часов', 12:'Двенадцать часов',13:'Один час', 
           14:'Два часа', 15:'Три часа', 16:'Четыре часа', 17:'Пять часов', 18:'Шесть часов', 19:'Семь часов', 
           20:'Восемь часов', 21:'Девять часов', 22:'Десять часов', 23:'Одиннадцать часов', 0:'Ноль часов'}  

hours_2 = {1:'первого', 2:'второго', 3:'третьего', 4:'четвертого', 5:'пятого', 6:'шестого', 7:'седьмого', 8:'восьмого', 
           9:'девятого', 10:'десятого', 11:'одиннадцатого', 12:'двенадцатого'} 

hours_3 = {1:'час', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять',
           11:'одиннадцать', 12:'двенадцать'}

minutes_1 = {1: 'Одна минута', 2: 'Две минуты', 3: 'Три минуты', 4: 'Четыре минуты', 5: 'Пять минут',
             6: 'Шесть минут', 7: 'Семь минут', 8: 'Восемь минут', 9: 'Девять минут', 10: 'Десять минут',
             11: 'Одиннадцать минут', 12: 'Двенадцать минут', 13: 'Тринадцать минут', 14: 'Четырнадцать минут',
             15: 'Пятнадцать минут', 16: 'Шестнадцать минут', 17: 'Семнадцать минут', 18: 'Восемнадцать минут',
             19: 'Девятнадцать минут', 20: 'Двадцать минут', 21: 'Двадцать одна минута', 22: 'Двадцать две минуты', 
             23: 'Двадцать три минуты', 24: 'Двадцать четыре минуты', 25: 'Двадцать пять минут', 26: 'Двадцать шесть минут', 
             27: 'Двадцать семь минут', 28: 'Двадцать восемь минут', 29: 'Двадцать девять минут', 31: 'Тридцать одна минута',
             32: 'Тридцать две минуты', 33: 'Тридцать три минуты', 34: 'Тридцать четыре минуты', 35: 'Тридцать пять минут', 
             36: 'Тридцать шесть минут', 37: 'Тридцать семь минут', 38: 'Тридцать восемь минут', 39: 'Тридцать девять минут', 
             40: 'Сорок минут', 41: 'Сорок одна минута', 42: 'Сорок две минуты', 43: 'Сорок три минуты', 44: 'Сорок четыре минуты'}

minutes_2 = {45: 'пятнадцати минут', 46: 'четырнадцати минут', 47: 'тринадцати минут', 48: 'двенадцати минут',
             49: 'одиннадцати минут', 50: 'десяти минут', 51: 'девяти минут', 52: 'восьми минут', 53: 'семи минут', 54: 'шести минут', 
             55: 'пяти минут', 56: 'четырех минут', 57: 'трех минут', 58: 'двух минут', 59: 'одной минуты'}


option_input = input('Choose your destiny!\nTo choose the current time type «1», type «2» to enter the time individually: ')

if option_input == ('1'):
         option_1 = datetime.datetime.now().time()
         option_1 = str(option_1).split(':')
         hh_1 = int(option_1[0])
         mm_1 = int(option_1[1])
         
         if mm_1 == 0:
                print(f'{hh_1:02}:{mm_1:02} - {hours_1[hh_1]} ровно.\nSee you later, alligator!')
         elif 0 < mm_1 < 30 or 30 < mm_1 < 45:
                print(f'{hh_1:02}:{mm_1:02} - {minutes_1[mm_1]} {hours_2[hh_1%12+1]}.\nSee you later, alligator!')
         elif mm_1 == 30:
                print(f'{hh_1:02}:{mm_1:02} - Половина {hours_2[hh_1%12+1]}.\nSee you later, alligator!')
         elif 45 <= mm_1 < 60:
                print(f'{hh_1:02}:{mm_1:02} - Без {minutes_2[mm_1]} {hours_3[hh_1%12+1]}.\nSee you later, alligator!')

elif option_input == ('2'):
      
        while True:
                time_imput = input('Please, enter the time in «hh:mm» format: ')
                if len(time_imput) != 5:
                        print('Error! The entry field must contain 5 symbols.')
                        continue
                if time_imput[2] != ":":
                        print('Error! The symbol «:» is absent.')
                        continue
                values = time_imput.split(':')
                hours, minutes = values[0], values[1]
                if not (hours.isdigit() and minutes.isdigit()):
                        print('Error! Please, enter the digits.')
                        continue
                hours, minutes = int(hours), int(minutes)
                if hours > 23 or minutes > 59:
                        print('Error! The hours should vary from 00 to 23 and the minutes should vary from 00 to 59.')
                        continue
                break
        
        option_2 = time_imput
        option_2 = str(option_2).split(':')
        hh_2 = int(option_2[0])
        mm_2 = int(option_2[1])
         
        if mm_2 == 0:
                print(f'{hh_2:02}:{mm_2:02} - {hours_1[hh_2]} ровно.\nSee you later, alligator!')
        elif 0 < mm_2 < 30 or 30 < mm_2 < 45:
                print(f'{hh_2:02}:{mm_2:02} - {minutes_1[mm_2]} {hours_2[hh_2%12+1]}.\nSee you later, alligator!')
        elif mm_2 == 30:
                print(f'{hh_2:02}:{mm_2:02} - Половина {hours_2[hh_2%12+1]}.\nSee you later, alligator!')
        elif 45 <= mm_2 < 60:
                print(f'{hh_2:02}:{mm_2:02} - Без {minutes_2[mm_2]} {hours_3[hh_2%12+1]}.\nSee you later, alligator!')
else:
     print ('Error! Please, try again.')
               
                
               

