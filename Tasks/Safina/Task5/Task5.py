#check_str
def check_str(line):
    upper_case = 0
    lower_case = 0
    for i in line:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    return f"('{line}') -> '{upper_case}' upper case, '{lower_case}' lower case'" 

print(check_str('The quick Brown Fox'))    

#is_prime
def is_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if (count <= 0):    
        return True
    else:
        return False     

print(is_prime(787)) 
print(is_prime(777)) 

#get_ranges
def get_ranges(x):
    number = 0
    list = []
    for i in range(len(x)):
        if i!= len(x)-1 and int(x[i] + 1) == x[i + 1]:
            number += 1
        elif number == 0: 
            list.append(f'{x[i]}')
        else:
            list.append(f'{x[i-number]}-{x[i]}')
            number = 0
    return ', '.join(list) 
    
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))

    