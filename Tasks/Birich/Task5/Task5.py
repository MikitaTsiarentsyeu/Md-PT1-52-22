with open("text.txt", 'r') as text_r:
    text = text_r.read()
    text_r.close()


def check_str(line_contents):
    uppers, lowers = 0, 0
    space, symbol = 0, 0
    for elem in line_contents:
        if elem.isupper() == True:
            uppers += 1
        elif elem.islower() == True:
            lowers += 1
        elif elem.isspace() == True:
            space += 1
        else:
            symbol += 1
    return f"\n('{line_contents}') -> '{uppers} upper case, {lowers} lower case, {space} space, {symbol} characters'"


data_strings = check_str(text)
print(data_strings)


def is_prime(number):
    if number <= 0:
        return f"\nInvalid number entered: {number}\nThe entered number must be equal to 1 or greater than 1"
    else:
        counter = 0
        for i in range(1, number+1):
            if number % i == 0:
                counter += 1
        if counter == 2:  # a number divisible by 1 and by itself is prime
            return f"\nis_prime({number}) -> {True}"
        else:
            return f"\nis_prime({number}) -> {False}"


vareable_num1 = is_prime(787)
vareable_num2 = is_prime(777)
print(vareable_num1, vareable_num2)


def get_ranges(input_list):
    if input_list != list():
        user_list = list(sorted(input_list))
        counter = 0
        resulting_list = list()

        for elem in range(len(user_list)):
            if elem != len(user_list)-1 and user_list[elem] + 1 == user_list[elem + 1]:
                counter += 1
            elif counter == 0:
                resulting_list.append(f"{user_list[elem]}")
            else:
                resulting_list.append(
                    f"{user_list[elem-counter]}-{user_list[elem]}")
                counter = 0
        return f'''\nget_ranges({user_list})  ->  "{', '.join(resulting_list)}"'''
    else:
        return f"\nYour list  ->  {resulting_list} is empty."


list_1 = get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
list_2 = get_ranges([4, 7, 10])
list_3 = get_ranges([2, 3, 8, 9])
print(list_1, list_2, list_3)
