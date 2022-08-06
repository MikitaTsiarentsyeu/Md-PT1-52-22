# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

s = str(input("Enter words using uppercase and lowercase: \n"))
if len(s) == 0:
    print("You have entered an empty string, please repeat the input")
else:    
    def check_str(s):
        d={"upper_case":0, "lower_case":0}
        for l in s:
            if l.isupper():
                d["upper_case"]+=1
            elif l.islower():
                d["lower_case"]+=1
            else:
                pass
        print (d["upper_case"], "upper case,", d["lower_case"], "lower case")
    check_str(s)


# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

n = float(input("Enter a number > 0:\n"))
if n <= 0:
    print("You entered a number <= 0")
elif n == 1:
    print("The number 1 is neither a prime nor a composite number, since it has only one divisor — 1.")
else:
    def is_prime(n):
        if n == 2 or n == 3: 
            print("is_prime", n, "-> ", end='')
            return True
        if n%2 == 0 or n < 2:
            print("is_prime", n, "-> ", end='')
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                print("is_prime", n, "-> ", end='')
                return False 
        print("is_prime", n, "-> ", end='')
        return True
    print(is_prime(n))


#     3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"