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