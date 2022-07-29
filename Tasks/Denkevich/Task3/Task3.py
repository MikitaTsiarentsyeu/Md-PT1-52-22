import datetime
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
     7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
     13: 'thirteen', 14: 'sixteen', 15: 'fifteen', 16: 'sexteen', 17: 'seventeen',
     18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
     23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
     29: 'twenty nine', 30: 'thirty', 31: 'thirty one', 32: 'trirty two', 33: 'thirty three', 34: 'thirty four',
     35: 'thirty five', 36: 'thirty six', 37: 'thirty seven', 38: 'thirty eight', 39: 'thirty nine', 40: 'fourty',
     41: 'fourty one', 42: 'fourty two', 43: 'fourty three', 44: 'fourty four', 45: 'fourty five', 46: 'fourty six',
     47: 'fourty seven', 48: 'fourty eight', 49: 'fourty nine', 50: 'fifty', 51: 'fifty one', 52: 'fifty two',
     53: 'fifty three', 54: 'fifty four', 55: 'fifty five', 56: 'fifty six', 57: 'fifty seven', 58: 'fifty eight',
     59: 'fifty nine', 60: 'sixty'}
currentTime = datetime.datetime.today().strftime('%H:%M')
n = 1
while True:
    inp = input('\n-------------------\nPlese if you want to know what time is it, enter 1.\nIf you want to input your time, enter 2.\n')
    if inp.isdigit():
        if int(inp) == 1:
            time = currentTime
        elif int(inp) == 2:
            userTime = input('Please enter the time in a format HH:MM:\n')
            time = userTime
        else:
            print('Your input is incorect. Try again.')
            print(f'   Log: {n} program executions')
            n += 1
            continue
        if time[0:2].isdigit() == False or time[2] != ':' or time[3:5].isdigit() == False or len(time) != 5:
            print('Incorrect time. Try again please.')
        elif int(time[0:2]) > 23 or int(time[3:5]) >= 60:
            print('Incorrect time. Try again please.')
        else:
            h = int(time[0:2])
            m = int(time[3:5])
            p = ''
            if h <= 12:
                if m == 0:
                    print(f'Its exactly {d[h]} oclock a.m.')
                if m >= 1 and m < 30:
                    print(f'{d[m][0].upper()}{d[m][1:]} minutes past {d[h]} a.m')
                if m == 30:
                    print(f'Half past {d[h]} a.m')
                if m > 30:
                    print(
                        f'{d[60 - m][0].upper()}{d[60 - m][1:]} minutes to {d[h]} a.m')
            elif h > 12:
                h = h - 12
                if m == 0:
                    print(f'Its exactly {d[h]} p.m. oclock.')
                    continue
                if m < 30:
                    print(
                        f'{d[m][0].upper()}{d[m][1:]} minutes past {d[h]} p.m.')
                if m == 30:
                    print(f'Half past {d[h]} p.m.')
                if m > 30:
                    print(
                        f'{d[60 - m][0].upper()}{d[60 - m][1:]} minutes to {d[h]} p.m.')
    print(f'   Log: {n} program executions')
    n += 1
