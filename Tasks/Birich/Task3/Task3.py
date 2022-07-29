import datetime

dictionary_of_minutes = {1: "одна", 2: "две", 3: "три", 4: "четыри", 5: "пять", 6: "шесть", 7: "семь", 8: "весемь", 9: "девять",
                         10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
                         15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
                         20: "двадцать", 21: "двадцать одна", 22: "двадцать две", 23: "двадцать три", 24: "двадцать четыре",
                         25: "двадцать пять", 26: "двадцать шесть", 27: "двадцать семь", 28: "двадцать восемь", 29: "двадцать девять",
                         31: "тридцать одна", 32: "тридцать две", 33: "тридцать три", 34: "тридцать четыре", 35: "тридцать пять",
                         36: "тридцать шесть", 37: "тридцать семь", 38: "тридцать восемь", 39: "тридцать девять", 40: "сорок",
                         41: "сорок одна", 42: "сорок две", 43: "сорок три", 44: "сорок четыре"}

dictionary_of_time = {1: "час", 13: "час", 2: "два", 14: "два", 3: "три", 15: "три", 4: "четыре", 16: "четыре", 5: "пять", 17: "пять",
                      6: "шесть", 18: "шесть", 7: "семь", 19: "семь", 8: "весемь", 20: "весемь", 9: "девять", 21: "девять",
                      10: "десять", 22: "десять", 11: "одинадцать", 23: "одинадцать", 12: "двенадцать", 24: "двенадцать"}

dictionary_of_numerals = {59: "одной", 58: "двух", 57: "трех", 56: "четырех", 55: "пяти", 54: "шести", 53: "семи",
                          52: "восьми", 51: "девяти", 50: "десяти", 49: "одинадцати", 48: "двенадцати",
                          47: "тринадцати", 46: "четырнадцати", 45: "пятнадцати"}

dictionary_of_numerals_time = {1: "первого", 13: "первого", 2: "второго", 14: "второго", 3: "третьего", 15: "третьего",
                               4: "четвертого", 16: "четвертого", 5: "пятого", 17: "пятого", 6: "шестого", 18: "шестого",
                               7: "седьмого", 19: "седьмого", 8: "восьмого", 20: "восьмого", 9: "девятого", 21: "девятого", 10: "десятого",
                               22: "десятого", 11: "одинадцатого", 23: "одинадцатого", 12: "двенадцатого", 24: "двенадцатого"}

print("\nВас приветсвует самоучитель: 'Счастливые часов не наблюдают'\nПопробуй ввести время верно и стань счастливым, но это неточно.\n")

while True:

    print("У Вас есть два варианта, чтобы узнать насущное время:\n    вариант №1 - помощь компьтера (цифра 1).\n    вариант №2 - ввести время вручную (цифра 2).")
    time_help = input("Пожалуйста, выберите вариант и введите цифру 1 или 2: ")
    variable = True
    variable_1 = "1"
    variable_2 = "2"

    if time_help == variable_1:
        current = datetime.datetime.now()
        current_time = current.strftime("%H:%M")
        hour_comp = int(current_time[0:2])
        minutes_comp = int(current_time[3:5])

        hour_exactly = dictionary_of_time.get(hour_comp)
        data_hours = dictionary_of_time.get(hour_comp+1)
        data_hours_of_numerals = dictionary_of_numerals_time.get(hour_comp+1)
        data_minutes_of_numerals = dictionary_of_numerals.get(minutes_comp)
        data_minutes = dictionary_of_minutes.get(minutes_comp)
# возникли проблемы с выводом
        if data_minutes in dictionary_of_minutes.values() and data_hours_of_numerals in dictionary_of_numerals_time.values():
            if minutes_comp == 1:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp:02d} - {data_minutes} минута {data_hours_of_numerals}.\n")
            elif 1 < minutes_comp < 5:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp:02d} - {data_minutes} минуты {data_hours_of_numerals}.\n")
            elif minutes_comp < 10:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp:02d} - {data_minutes} минут {data_hours_of_numerals}.\n")
            elif minutes_comp == 21 or minutes_comp == 31 or minutes_comp == 41:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp} - {data_minutes} минута {data_hours_of_numerals}.\n")
            elif 21 < minutes_comp < 25:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp} - {data_minutes} минуты {data_hours_of_numerals}.\n")
            elif minutes_comp >= 10:
                print(
                    f"\n{hour_comp:02d}:{minutes_comp} - {data_minutes} минут {data_hours_of_numerals}.\n")
        elif minutes_comp == 59:
            print(
                f"\n{hour_comp:02d}:{minutes_comp} - без {data_minutes_of_numerals} минуты {data_hours}.\n")
        elif minutes_comp >= 45:
            print(
                f"\n{hour_comp:02d}:{minutes_comp} - без {data_minutes_of_numerals} минут {data_hours}.\n")
        elif minutes_comp == 0 and hour < 5:
            print(
                f"\n{hour_comp:02d}:{minutes_comp:02d} - {hour_exactly} часа ровно.\n")
        elif minutes_comp == 30:
            print(
                f"\n{hour_comp:02d}:{minutes_comp} - половина {data_hours_of_numerals}.\n")

    elif time_help == variable_2:
        time_token = input(
            "\nПожалуйста введите данные в формате времени(hh:mm): ")
        if len(time_token) != 5:
            print(
                f"Ваш ввод: ({time_token}) не соответсвует формату времени(hh:mm).\n")
            continue
        elif time_token[2] != ":":
            print(
                f"Ваш ввод: ({time_token}) не соответсвует формату времени(hh:mm).\n")
            continue
        values_token = time_token.split(':')
        hour, minutes = values_token[0], values_token[1]
        if not (hour.isdigit() and minutes.isdigit()):
            print(
                f"Ваш ввод: ({time_token}) не соответсвует формату времени(hh:mm).\n")
            continue
        hour, minutes = int(hour), int(minutes)
        if hour > 23 or minutes > 59:
            print(
                f"\nВаш ввод: {hour:02d}(hh):{minutes:02d}(mm) не соответсвуют формату времени:\n\
    (hh) - c 00 до 23 часов;\n    (mm) - c 00 до 59 минут.\n")
            continue

        hour_exactly = dictionary_of_time.get(hour)
        data_hours = dictionary_of_time.get(hour+1)
        data_hours_of_numerals = dictionary_of_numerals_time.get(hour+1)
        data_minutes_of_numerals = dictionary_of_numerals.get(minutes)
        data_minutes = dictionary_of_minutes.get(minutes)
# возникли проблемы с выводом
        if data_minutes in dictionary_of_minutes.values() and data_hours_of_numerals in dictionary_of_numerals_time.values():
            if minutes == 1:
                print(
                    f"\n{hour:02d}:{minutes:02d} - {data_minutes} минута {data_hours_of_numerals}.\n")
            elif 1 < minutes < 5:
                print(
                    f"\n{hour:02d}:{minutes:02d} - {data_minutes} минуты {data_hours_of_numerals}.\n")
            elif minutes < 10:
                print(
                    f"\n{hour:02d}:{minutes:02d} - {data_minutes} минут {data_hours_of_numerals}.\n")
            elif minutes == 21 or minutes == 31 or minutes == 41:
                print(
                    f"\n{hour:02d}:{minutes} - {data_minutes} минута {data_hours_of_numerals}.\n")
            elif 21 < minutes < 25:
                print(
                    f"\n{hour:02d}:{minutes} - {data_minutes} минуты {data_hours_of_numerals}.\n")
            elif minutes >= 10:
                print(
                    f"\n{hour:02d}:{minutes} - {data_minutes} минут {data_hours_of_numerals}.\n")
        elif minutes == 59:
            print(
                f"\n{hour:02d}:{minutes} - без {data_minutes_of_numerals} минуты {data_hours}.\n")
        elif minutes >= 45:
            print(
                f"\n{hour:02d}:{minutes} - без {data_minutes_of_numerals} минут {data_hours}.\n")
        elif minutes == 0 and hour < 5:
            print(f"\n{hour:02d}:{minutes:02d} - {hour_exactly} часа ровно.\n")
        elif minutes == 30:
            print(f"\n{hour:02d}:{minutes} - половина {data_hours_of_numerals}.\n")
    else:
        print(
            f"\nВот, что вы ввели - ({time_help}), будьте внимательны при вводе данных.\n")
    if variable == True:
        question = input(
            "Вы хотите еще раз попытать счастье: да/нет?\n    если да, нажмите(+).\n    елси нет, нажмите(-).\n")
        symbol_pl = "+"
        symbol_mn = "-"
        if question == symbol_pl:
            print("\nС удовольствием утолим Ваше любопытсво!!!\n")
            continue
        elif question == symbol_mn:
            print("\nУдача была так близка!\n")
        else:
            print(
                f"\nВот, что вы ввели - ({question}), будьте внимательны при вводе данных.\n")
            continue

    break
