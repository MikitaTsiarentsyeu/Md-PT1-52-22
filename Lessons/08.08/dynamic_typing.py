def times(a:object, b:object) -> object:
    return a*b

def times_for_int(a:int, b:int) -> int:
    "this function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int(2, 4))
print(times_for_int(2.0, 4.0))

print(times(2, 4))
print(times(2.0, 4.0))
print(times([2], 4))
print(times('2', 4))

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq([1,2,3], (1,3,2,3)))
print(eq(['1','2','3'], "123"))


def sum(a, b):
    return a+b

def sum(a, b, c):
    return sum(a, b) + c #error the sum(a,b) does not exist

sum(3, 4, 5)