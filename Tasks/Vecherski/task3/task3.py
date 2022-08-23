from datetime import datetime
import re

text =  {1:"одна", 2:"две", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 
        10:"десять", 11:"одиннадцать", 12 and 00:"двенадцать", 13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать",
        16:"шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать", 20:"двадцать", 
        21:"двадцать одна", 22:"двадцать две", 23:"двадцать три", 24:"двадцать четыре", 25:"двадцать пять", 
        26:"двадцать шесть", 27:"двадцать семь", 28:"двадцать восемь", 29:"двадцать девять", 30:"тридцать",
        31:"тридцать одна", 32:"тридцать две", 33:"тридцать три", 34:"тридцать четыре", 35:"тридцать пять", 
        36:"тридцать шесть", 37:"тридцать семь", 38:"тридцать восемь", 39:"тридцать девять", 40:"сорок", 
        41:"сорок одна", 42:"сорок две", 43:"сорок три", 44:"сорок четыре",45:"сорок пять", 46:"сорок шесть", 
        47:"сорок семь", 48:"сорок восемь", 49:"сорок девять", 50:"пятьдесят", 51:"пятьдесят одна", 
        52:"пятьдесят две", 53:"пятьдесят три", 54:"пятьдесят четыре", 55:"пятьдесят пять", 56:"пятьдесят шесть",
        57:"пятьдесят семь", 58:"пятьдесят восемь", 59:"пятьдесят девять"}

infin = {1:"один", 2:"два"}

rodit_plur = {59:"одной", 58:"двух", 57:"трех", 56:"четырех", 55:"пяти", 54:"шести", 53:"семи", 52:"восьми",
             51:"девяти", 50:"десяти", 49:"одиннадцати", 48:"двенадцати", 47:"тринадцати", 46:"четырнадцати", 
             45:"пятнадцати"}

rodit_sing = {1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 
             8:"восьмого", 9:"девятого", 10:"десятого", 11:"одиннадцатого", 12:"двенадцатого"}

while True:
    choose = input(f"enter 1 to convert current time to words or enter 2 to put your time and convert\n")
    if choose == '1' or choose == '2':
        break
    else:
        print(f'wrong number, try one more time, Bro')
        continue

if choose == '1':
    hr = datetime.now().hour%12                           #(int(datetime.now().strftime("%I")))%12                
    min = datetime.now().minute
else:
    time = input(f'Enter your time in format HH:MM\n')
    while not re.findall(r'^\d\d\:\d\d$',time) or int(time.split(':')[0]) >= 25 or int(time.split(':')[1]) > 59:
            time = input(f'wrong input, thy again (Format HH:MM)\n')
            continue
    hr = int(time.split(':')[0])%12                                     
    min = int(time.split(':')[1])
   
if min == 0:
    if hr == 0 or 5 <= hr <= 11:
        print(f"{text[hr]} часов ровно")
    elif hr == 1:
        print(f"{infin[hr]} час ровно")
    elif hr == 2:
        print(f"{infin[hr]} часа ровно")
    else:
        print(f"{text[hr]} часа ровно")
elif min == 1 or min == 21 :
    print(f"{text[min]} минута {rodit_sing[hr+1]}")
elif 2<= min <= 4 or 22 <= min <= 24:
    print(f"{text[min]} минуты {rodit_sing[hr+1]}")
elif 5 <= min <= 20 or 25 <= min <= 29:
    print(f"{text[min]} минут {rodit_sing[hr+1]}")
elif min == 30:
    print(f"половина {rodit_sing[hr+1]}")
elif min == 41 or min == 31:
    print(f"{text[min]} минута {rodit_sing[hr+1]}")
elif 32 <= min <= 34 or 42 <= min <= 44:
    print(f"{text[min]} минуты {rodit_sing[hr+1]}")
elif 35 <= min <= 40:
    print(f"{text[min]} минут {rodit_sing[hr+1]}")
elif min == 59:
    print(f"без {rodit_plur[min]} минуты {rodit_sing[hr+1]}")
else:
    print(f"без {rodit_plur[min]} минут {rodit_sing[hr+1]}")

