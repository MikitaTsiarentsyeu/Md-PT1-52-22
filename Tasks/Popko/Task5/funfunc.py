def check_str(first):
    upper_num = 0
    lower_num = 0
    if len(first) > 0:
        for elem in first:
            if elem.isupper():
                upper_num = upper_num + 1
            if elem.islower():
                lower_num = lower_num + 1
        print(f"{upper_num} upper case, {lower_num} lower case ")
        return first
x = input ('Please enter your name:\n')
print ('Hello,', x, end = '!\n')
check_str(input('Please enter the phrase:\n'))
    
def isPrime(second):
    devider_num = 0
    for i in range(2, round(second / 2) + 1):
        if (second % i == 0):
            devider_num = devider_num + 1
    if (devider_num <= 0):
        print ("It's correct\n")
    else:
        print ("It's incorrect\n")
isPrime(int(input('Please enter a prime number greater than zero:\n')))

def get_ranges(third):
    list_new = []
    for i in third:
        if i != third[0] + 1:
            list_new.append([i])
        elif len(list_new[-1]) > 1:
            list_new[-1][-1] = i
        else:
            list_new[-1].append(i)
        third[0] = i
    return (', '.join(['-'.join(map(str, det)) for det in list_new]))
print('Take a look for the last one:\n')
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))






                

