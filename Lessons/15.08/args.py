x, y = 2, 3

def func(x, y):
    x[0] += y
    print(x, y)

l = [2]
func(l, y)
print(l, y)

def evaluate(arg1, arg2, arg3):
    return arg1+arg2*arg3

print(evaluate(2, 3, 4))
print(evaluate(arg3=2, arg2=3, arg1=4))
print(evaluate(2, 3, arg3=4))

def evaluate(arg1, arg2, arg3=4):
    return arg1+arg2*arg3

print(evaluate(1,2))
print(evaluate(arg2=0, arg1=3))


def sum(*args):
    print(type(args))
    print(args)
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
l = [1,2,3,4,5]
print(sum(*l))

def sum(**kwargs):
    print(type(kwargs))
    print(kwargs)
    res = 0
    for i in kwargs.values():
        res += i
    return res

d = {"one":1, "two":2}
print(sum(**d))
print(sum(one=1,two=2,three=3,four=4,five=5))

def my_print(*args, sep=" ", end="\n"):
    print(sep, end)
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,5,6,7,8,9, sep=",", end=".")


def my_print(*args, **kwargs):
    print(args, kwargs)
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,6,7,8,9, sep=",", end=".")