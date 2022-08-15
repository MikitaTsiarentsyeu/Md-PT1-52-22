# while True:
#     print("I'm going!!!")

# def cycle():
#     print("I'm going!!!")
#     cycle()


# cycle()


def level1():
    print("level 1 is starting")
    level2()
    print("level 1 is done")

def level2():
    print("level 2 is starting")
    level3()
    print("level 2 is done")

def level3():
    print("level 3 is starting")
    level4()
    print("level 3 is done")

def level4():
    print("level 4 is starting")
    print("level 4 is done")


# level1()

def level(n):
    print(f"level {n} is starting")
    if n != 0:
        level(n-1)
    print(f"level {n} is done")

level(4)

1*2*3*4*5

def factorial(n):
    if n == 1:
        return 1
    c = factorial(n-1)
    return n*c

print(factorial(1))
print(factorial(3))
print(factorial(5))
print(factorial(7))



def digits_sum(n):
    if n == 0:
        return 0
    rem = n % 10
    return rem + digits_sum(n//10)

print(digits_sum(12345))

