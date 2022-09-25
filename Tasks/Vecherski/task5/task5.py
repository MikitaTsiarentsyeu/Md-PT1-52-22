import re

def check_str(string):
    result_lower = 0
    result_upper = 0
    if not string:
        return print("The string in empty")
    for i in re.findall(r"[A-ZА-Я]",string): 
        result_upper += 1
    for i in re.findall(r"[a-zа-я]",string): 
        result_lower += 1
    return print(f'in lower case {result_lower} letter(s), in upper case {result_upper} letter(s)')

inputed_string = input(f'Type not empty string to check how much letters in upper and lower case:\n')
check_str(inputed_string)

#==============================================================================

def is_prime(number):
    try:
        number = int(number)
        if number == 1:
            return print(False) 
        for i in range(2,number // 2 + 1):
            if number % i == 0:
                return print(False)
        return print(True)
    except:
        return print("Not natural")

inputed_number = input('enter a positive number to check if it is prime:\n')
is_prime(inputed_number)

#==============================================================================

def get_ranges(list):
    new_list = []
    for i in list:
        if i != list[0] + 1:
            new_list.append([i])
        elif len(new_list[-1]) > 1:
            new_list[-1][-1] = i
        else:
            new_list[-1].append(i)
        list[0] = i
    return print((', '.join(['-'.join(map(str, elem)) for elem in new_list])))

inputed_list = list(map(int,(input('enter your list of numbers separated by commas\n')).split(",")))
get_ranges(inputed_list)