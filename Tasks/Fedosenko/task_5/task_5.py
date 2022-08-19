
def check_str(string_to_test):
    counter_lower = 0
    counter_upper = 0
    if len(string_to_test) == 0:
        print('Empty string')
    else:

        for char in string_to_test:
            if char >= "a" and char <= "z":
                counter_lower += 1
            elif  char >= "A" and char <= "Z":
                counter_upper += 1
        print(f"{counter_upper} upper case, {counter_lower} lower case ")
        return string_to_test

check_str(input("Enter the string\n"))


def isPrime(x):
    divisor_counter = 0
    for i in range(2, x):
        if (x % i == 0):
            divisor_counter = divisor_counter+1
    if (divisor_counter <= 0):
        print("True")
    else:
        print("False")

isPrime(int(input("Enter the number\n")))

def get_ranges(list_of_numbers):
    
    counter = 0
    new_list = []
    for i in range(len(list_of_numbers)):
        if i!= len(list_of_numbers)-1 and int(list_of_numbers[i] + 1) == list_of_numbers[i + 1]:
            counter += 1
        elif counter == 0: 
            new_list.append(str(list_of_numbers[i])) 
        else:
            new_list.append(f'{list_of_numbers[i-counter]}-{list_of_numbers[i]}')
            counter = 0
    return ', '.join(new_list)            


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))