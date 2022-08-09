def check_str(s):
    lower = 0
    upper = 0
    for i in range(len(s)):
       if s[i].islower():
           lower += 1
       if s[i].isupper():
           upper += 1
    s = f"{upper} upper case, {lower} lower case."
    return print(s)

check_str('The quick Brown Fox')

def is_prime(number):
    if number < 2: 
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(787))
print(is_prime(777))

def get_ranges(l):
    if l == []:
        return "list is empty"
    if len(l) == 1:
        return f"{l[0]}"
    l = list(sorted(set(l)))
    res = ""
    res = res + f"{l[0]}"
    for i in range(1, len(l)-1):
        if l[i-1] == l[i] - 1 and l[i+1] == l[i] + 1:
            pass
        elif l[i-1] == l[i] - 1 and l[i+1] != l[i] + 1:
            res = res + "-" + f"{l[i]}" + ", "
        elif l[i-1] != l[i] - 1 and l[i+1] != l[i] + 1:
            res = res + ", " + f"{l[i]}" + ", "
        else:
            res = res + f"{l[i]}" 
    if l[len(l)-1] == l[len(l)-2] + 1:
        res = res + "-" + f"{l[len(l)-1]}" 
    else:
        res = res + f"{l[len(l)-1]}" 
    return res  
        
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))