
def check_str(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isalpha():
            if char.lower() == char:
               lower+=1
            else:
                upper+=1   
        else:
            pass
    print(f'{upper} upper case, {lower} lower case')

check_str('The quick BRown,        Fpppppox?')

def is_prime(number):
    if number == 1:
        return False 
    for i in range(2,number//2+1):
        if number % i == 0:
           return False
    return True
print(is_prime(787))    

def get_ranges(list):
    n = 0
    mas = []
    start = 0
    for i in range(0,len(list)-1):
        if list[i] + 1 == list[i+1]:
            if n == 0:
                start = list[i]
                n = 1
            pass   
        else:
            if n == 1:
               finish = list[i]
               mas.append(f'{start}-{finish}')
               n=0
               start = 0
            else:
                mas.append(f'{list[i]}')  
    if start != 0:
        mas.append(f'{start}-{list[-1]}')
    else:
        mas.append(f'{list[-1]}')               
    return ','.join(mas)

print(get_ranges([2,4,9,10]))