import random

my_number = random.randint(1, 10)

your_number = int(input("Guess my number:\n"))

if your_number == my_number:
    print("Correct!")
else:
    print("Loooooooser!!!")