import time

def timer(func):
    def wrapper(n):
        start = time.time()
        res = func(n)
        finish = time.time()
        global t
        t = finish - start
        return res
    return wrapper

@timer
def loader(n):
    r = 0
    for i in range(n):
        r += i
    return r


print(loader(1000000))
print(t)