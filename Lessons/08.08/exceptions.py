
l = [1,2,3]

try:
    10/0
    l[3] = 4
    print(x)
except NameError as e:
    print("some undefined variable detected")
    print(e)
except IndexError as e:
    print("incorrect index usage detected")
    print(e)
except:
    print("something went wrong, but I don't know what")

print("the rest of the program goes here")