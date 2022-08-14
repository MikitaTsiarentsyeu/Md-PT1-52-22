# solution 1
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

# solution 2
for i in range (1,101):
    print("Fizz"*(i%3==0)+(i%5==0)*"Buzz" or i)

# solution 3
print("\n".join(["Fizz"*(i%3==0)+(i%5==0)*"Buzz" or str(i) for i in range(1,101)]))

# solution 4
def FizzBuzz(max_num, x, y):
    for i in range(1, max_num):
        output = ""
        if i % x == 0:
            output += "Fizz"
        if i % y == 0:
            output += "Buzz"
        print(output or i)

FizzBuzz(101, 3, 5)