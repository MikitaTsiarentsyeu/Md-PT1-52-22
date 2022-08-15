def check_str(a):
    u,l = 0,0
    for i in a:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    return f'{u} upper case, {l} lower case'

print (check_str('The quick Brown Fox')) 

def is_prime(b):
    for i in range (2,b):
        if b%i == 0:
            return False
    return True

print(is_prime(787)) 
print(is_prime(777)) 

def get_ranges(c):
    s=''
    while len(c)>1:
        if c[1] == c[0]+1:
            s+=f'{c[0]} - '
            while len(c)>1 and c[1] == c[0]+1:
                c.pop(0)
        s+=f'{c.pop(0)}, '
    if len(c)>0:
        s+=f'{c[0]}'
    return s.strip(' ,')

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  
print(get_ranges([4,7,10])) 
print(get_ranges([2, 3, 8, 9])) 