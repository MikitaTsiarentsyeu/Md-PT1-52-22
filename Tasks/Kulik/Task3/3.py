import datetime
d = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 
     11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать',
     18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 21: 'двадцать один', 22: 'двадцать два',
     23: 'двадцать три', 24: 'двадцать четыре', 25: 'двадцать пять', 26: 'двадцать шесть', 27: 'двадцать семь', 28: 'двадцать восемь',
     29: 'двадцать девять', 30: 'тридцать', 31: 'тридцать один', 32: 'тридцать две', 33: 'тридцать три', 34: 'тридцать четыре',
     35: 'тридцать пять', 36: 'тридцать шесть', 37: 'тридцать семь', 38: 'тридцать восемь', 39: 'тридцать девять', 40: 'сорок',
     41: 'сорок одна', 42: 'сорок две', 43: 'сорок три', 44: 'сорок четыре', 45: 'сорок пять', 46: 'сорок шесть', 47: 'сорок семь', 
     48: 'сорок восемь', 49: 'сорок девять', 50: 'пятьдесят', 51: 'пятьдесят один', 52: 'пятьдесят два',
     53: 'пятьдесят три', 54: 'пятьдесят четыре', 55: 'пятьдесят пять', 56: 'пятьдесят шесть', 57: 'пятьдесят семь', 58: 'пятьдесят восемь',
     59: 'пятьдесят девять', 60: 'шестьдесят'}
d1 = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвёртого', 5: 'пятого', 6: 'шестого', 7: 'седьмого', 8: 'восьмого',
      9: 'девятого', 10: 'десятого', 11: 'одинадцатого', 12: 'двенадцатого'}
d2 = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре'}
d3 = {59: 'одной', 58: 'двух', 57: 'трёх', 56: 'четырёх', 55: 'пяти', 54: 'шести', 53: 'семи', 52: 'восьми', 51: 'девяти',
      50: 'десяти', 49: 'одинадцати', 48: 'двенадцати', 47: 'тринадцати', 46: 'четырнадцати', 45: 'пятнадцати'}
      
x = input("Для текстового вывода текущего времени нажмите '1'.\nЧтобы получить текстовый вывод времени, введённого вручную, нажмите '2'.") 
if x == '1':
              current_time1 = datetime.datetime.now().time()
              current_time1 = str(current_time1).split (':')
              hour1 = int(current_time1[0])
              min1 = int(current_time1[1])
              
              if min1 == 0:
                  print(f"{d[hour1]} часов ровно")
            
              elif 0 < min1 < 30 or 30 < min1 < 45:
                  print(f"{d[min1]} минут(а) {d1[hour1%12+1]}")
              elif min1 == 30:
                  print (f"половина{d1[hour1%12+1]}")
              elif 45 <= min1 <60:
                  print (f"Без {d3[min1]} минут(а) {d[hour1%12+1]}")        
      
elif x == '2':

      while True:
             time_input = input('Введите время используя формат чч:мм.\n')
             if len (time_input) !=5:
                  print('Введите четырехзначнок значение')
                  continue
             if time_input[2] != ":":
                  print('введите символ двоеточие:')
                  continue
             values = time_input.split (':')
             hours, minutes = values[0], values[1]
             if not (hours.isdigit() and minutes.isdigit()):
                  print('введите цифры')
                  continue
             hours, minutes = int(hours), int(minutes)
             if hours > 23 or minutes > 59:
                  print ('серьезно? Введите максимум 24 часа и 60 минут')
                  continue
             break


      time2 = time_input
      time2 = str(time2).split (':')
      hour2 = int(time2[0])
      min2 = int(time2[1])
              
      if min2 == 0:
             print(f"{d[hour2]} часов ровно")
      elif min2 <= 4:
             print(f"{d2[min2]} минута(ы) {d1[hour2%12+1]}")
      elif 5 <= min2 < 30 or 30 < min2 < 45:
             print(f"{d[min2]} минут(а) {d1[hour2%12+1]}")
      elif min2 == 30:
            print (f"половина {d1[hour2%12+1]}")
      elif 45 <= min2 <60:
                  print (f"Без {d3[min2]} минут {d[hour2%12+1]}") 

        
        
       
else: 
    print ('Ошибка. Сделайте выбор.')