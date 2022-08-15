def check_str(text):
    count_lower = 0
    count_upper = 0
    if len(text) == 0:
        print("Your string is empty")
    else:
        for i in text:
            if i.isupper():
                count_upper += 1
            elif i.islower():
                count_lower += 1
        print(f"{text} -> {count_upper} upper case, {count_lower} lower case" )       
check_str(input("Please, enter your text\n"))

def is_prime(number):
    count = 0
    for i in range(2, number//2 + 1):
        if number % i == 0:
            count += 1
    if (count <= 0):
        print("True")
    else:
        print("False")
is_prime(int(input("Enter the number\n")))

def get_ranges(new_list):
    num = 0
    list = []
    for i in range(len(new_list)):
        if i!= len(new_list)-1 and int(new_list[i] + 1) == new_list[i + 1]:
            num += 1
        elif num == 0: 
            list.append(str(new_list[i])) 
        else:
            list.append(f'{new_list[i-num]}-{new_list[i]}')
            num = 0
    return ', '.join(list)            
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))

