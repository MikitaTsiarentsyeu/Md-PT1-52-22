x = 1

if x == 1:
    print("one")
    print("one")
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
# elif x == 5:
#     print("five")
else:
    print("IDK")



if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

if x > 0 or x == 0:
    if x == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")