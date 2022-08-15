
l = [1,2,3]

try:
    raise KeyError("the key was not found")
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
    raise NameError("name error from except?")
    print("something went wrong, but I don't know what")
finally:
    raise NameError("name error from finally")
    print("hello from finally")


print("the rest of the program goes here")

# with open("test.txt") as f: pass

# try:
#     f = open("test.txt")
# finally:
#     f.close()