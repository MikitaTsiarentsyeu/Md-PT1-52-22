def check_str(str_exampl):
    upper_case = 0
    lower_case = 0

    for i in range(len(str_exampl)):
        if str_exampl[i].isupper():
            upper_case +=1
        elif str_exampl[i] == " ":
            pass
        else:
            lower_case +=1
    return f"'{upper_case} upper case, {lower_case} lower case'"

print(check_str('The quick Brown Fox'))


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number

print(is_prime(787))
print(is_prime(777))


def get_ranges(list_exampl):
    temp_list = []
    number_counter = 0
    for i in range(len(list_exampl)):
        if i != len(list_exampl)-1 and list_exampl[i+1]-list_exampl[i] == 1:
            number_counter += 1
        elif number_counter == 0:
             temp_list.append(str(list_exampl[i]))   
        else:
            temp_list.append(f'{list_exampl[i-number_counter]}-{list_exampl[i]}')  
            number_counter = 0 
    temp_str = f"\"{', '.join(temp_list)}\""
    return temp_str

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))