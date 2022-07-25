from datetime import datetime

h = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого", 7: "седьмого", 8: "восьмого", 9: "девятого", 
10: "десятого", 11: "одиннадцатого", 12: "двеннадцатого", 13: "первого", 14: "второго", 15: "третьего", 16: "четвертого", 17: "пятого",
18: "шестого", 19: "седьмого", 20: "восьмого", 21: "девятого", 22: "десятого",  23: "одиннадцатого", 24: "двеннадцатого"}

while True:
   x = input("Выберите режим работы программы:\n Чтобы получить текстовый вывод текущего времени, нажмите 1.\n Чтобы получить текстовый вывод времени, введённого с консоли, нажмите 2.\n Для выхода нажмите 3.\n")
   if x == '1':
     current_time = datetime.now().time()
     hour = current_time.hour
     min = current_time.minute
   elif x == '3':
     exit()
   elif x == '2':
     current_time = str(input("Введите время в формате (hh:mm):\n"))
     if ":" in current_time:
         c = current_time.split(":")
     else: 
         print("Введенное время не соотвествует указанному формату.")
         continue
     if c[0].isdigit() and c[1].isdigit():
        hour = int(c[0]) 
        min = int(c[1])  
        if len(c[0]) == 2 and len(c[1]) == 2: 
            pass
        else: 
            print("Введенное время не соотвествует указанному формату.")
            continue
     else:
            print("Введенное время не соотвествует указанному формату.")
            continue
   else:
       print("Нажмите 1 или 2 для выбора режима работы программы. Нажмите 3 для выхода.")
       continue
   if min == 0:
    d = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
    11: "одиннадцать", 12: "двеннадцать", 13: "один", 14: "два", 15: "три", 16: "четыре", 17: "пять", 18: "шесть", 19: "семь", 
    20: "восемь", 21: "девять", 22: "десять",  23: "одиннадцать", 24: "двенадцать"}
    if (hour >= 2 and hour <= 4) or (hour >= 14 and hour <= 16):
         print(f"Сейчас {d.get(hour)} часа ровно.")
    elif hour == 1 or hour == 13:
         print(f"Сейчас час ровно.")
    else:
         print(f"Сейчас {d.get(hour)} часов ровно.")
   elif (min < 30) or (min > 30 and min < 45):
     m = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
     11: "одиннадцать", 12: "двеннадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 
     18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок"}
     tens, below_ten = divmod(min, 10)
     if min == 1 or min == 21 or min == 31 or min == 41:
          print(f"Сейчас {m.get(tens*10,'')} {m.get(below_ten)} минута {h.get(hour+1)}.\n")
     elif (min >= 2 and min <= 4) or (min >= 22 and min <= 24) or (min >= 32 and min <= 34) or (min >= 42 and min <= 44):
          print(f"Сейчас {m.get(tens*10,'')} {m.get(below_ten)} минуты {h.get(hour+1)}.\n")
     elif min >= 5 and min <= 19:
          print(f"Сейчас {m.get(min)} минут {h.get(hour+1)}.\n")
     else:
          print(f"Сейчас {m.get(tens*10)} {m.get(below_ten)} минут {h.get(hour+1)}.\n")
   elif min == 30:
      print(f"Сейчас половина {h.get(hour+1)}.\n")
   elif min >= 45:
     d = {1: "час", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять",
     11: "одиннадцать", 12: "двеннадцать", 13: "час", 14: "два", 15: "три", 16: "четыре", 17: "пять", 18: "шесть", 19: "семь", 
     20: "восемь", 21: "девять", 22: "десять",  23: "одиннадцать", 24: "двенадцать"}
     m = {59: "одной", 58: "двух", 57: "трех", 56: "четырех", 55: "пяти", 54: "шести", 53: "семи", 52: "восьми", 51: "девяти", 50: "десяти",
     49: "одиннадцати", 48: "двеннадцати", 47: "тринадцати", 46: "четырнадцати", 45: "пятнадцати"}
     if min == 59:
          print(f"Сейчас без {m.get(min)} минуты {d.get(hour+1)}.")
     else:
          print(f"Сейчас без {m.get(min)} минут {d.get(hour+1)}.")