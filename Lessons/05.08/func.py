# test_sum(3, 5)

def test_sum(a, b):
    print(id(a), id(b))
    res = a + b
    return res
    print("after return")

def test_print(val):
    # return
    print(val.upper())

new_test_sum = test_sum
print(id(test_sum), id(new_test_sum))


x, y = 33, 44
print(id(x), id(y))
r = test_sum(x, y)
print(type(r))

print(type(test_sum("test ", "string")))

r = test_print("hello")
print(type(r))


# def func(q, w, e, r, t, y):
#     print(q, w, e, r, t, y)

# def func(q):
#     print(q)

# func(1, 2) OVERRIDING

# sign = "*"
# if sign == "+":
#     def func(x, y):
#         return x+y
# elif sign == "*":
#     def func(x, y):
#         return x*y BAD APPROACH

def func(x, y, sign):
    if sign == "+":
        return x+y
    elif sign == "*":
        return x*y

print(func(3, 4, "+"))

def check_int(x):
    print(id(x))
    x += 2
    print(id(x))
    return x

y = 4
check_int(y)
print(id(y), y)

y = 4
y = check_int(y)
print(id(y), y)

def check_list(x):
    x[0] += 2

y = [4]
check_list(y)
print(id(y), y)

l = [3,2,5,7,4,3,8]
l_sorted = sorted(l)
l.sort()
print(l_sorted, l)



def canonical_mult(a, b):
    if b < 0:
        b = -b
        a = -a
    res = 0
    for i in range(b):
        res += a
    return res

print(canonical_mult(2, 3))
print(canonical_mult(0, 3))
print(canonical_mult(2, 0))
print(canonical_mult(0, 0))
print(canonical_mult(-2, 3))
print(canonical_mult(2, -3))
print(canonical_mult(-2, -3))