from functools import reduce

def apply(l, f, index=0):
    if index == len(l):
        return
    l[index] = f(l[index])
    apply(l, f, index+1)

l = [1,2,3,4,5]
# apply(l, str)
print(l)

def sq(x):
    return x*x

apply(l, sq)
print(l)

new_sq = lambda x: x*x
print(new_sq(3))

print((lambda x: x*x)(3))

apply(l, lambda x: x*x)
print(l)

lambda x, y: x+y

test_str = "Abc Aac aaa ttt kit kot"
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=lambda x: x[1]))

d = {"one":1, "two":2, "three":3}
print(sorted(d))
print(sorted(d, key=lambda x: d[x]))
print(sorted(d, key=d.get))
print(sorted(d.items(), key=lambda x: x[1]))


l = [1,2,3,4,5,6,7,8,9,10]
res = map(print, l)
print(res)
res = list(res)
print(res)

print(list(map(lambda num: chr(num*11), l)))

print(list(map(sq, l)))

print(list(filter(lambda x: x>5, l)))

print(list(map(lambda num: chr(num*11), filter(lambda x: x>5, l))))

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: x if x>=y else y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))

l=['1', '11', '12', '22', '2', '13', '30', '33'] 

print(sorted(filter(lambda x: int(x)%2 == 0, l), key=int))
