l = []
l = [1,2,3,4,5,"six",7.0,[]]
print(l)
print(type(l))

print(list("my test string"))

print([1,2,3]+[3,2,1])
print([0]*8)
print(len(l))

print(l[len(l)-1])
print(l[0], l[1], l[2])
print(l[0:7:2])
print(l[-1])
print(l[::-1])

l[0] = 1.0
print(l)

l.append("new elem")
print(l)

l.extend("new elem")
print(l)

l.insert(0, "new first elem")
print(l)

l.insert(1, "new second elem")
print(l)

l.insert(1000000, "new last elem")
print(l)

l[2:2] = [-1, 0]
print(l)

l[:12] = []
print(l)

l.remove('new elem')
print(l)

l.remove('e')
print(l)

print('e' in l)

if 4 in l:
    l.remove(4)
    print(l)

print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)

print(l.pop(0))
print(l)
print(l.pop(0))
print(l)

del l[0]
print(l)

l = [1,2,3,4,5,6]

del l[2:5]
print(l)

# del l
# print(l)

l.clear()
print(l)

l1 = l2 = []
# l2 = []
# l1 = l2 the same
l1.append(0)
print(l1, l2)

del l1
print(l2)


t = (1,2,3,4,5,"six",7.0,[],"last element")
print(type(t), t)

x = (1,)
print(type(x))
print(x)
# print(x[1]) error

print(len(t), t[3], ((1,2,3)+(4,5,6))*4)
print(t[1:6:2])

# t[0] = 1.0 error
# t.append(10) error

print(t.index('six'))
if '' in t:
    print(t.index(''))

del t

t = ([1,2,3],)
t[0].append(4)
print(t)

x = "str"
t = (x,)
x = 4
print(t)

x = [1,2,3]
t = (x,)
x.append(4)
print(t)



d = {}
d = {"one":1, "two": 2, 3:"three"}
print(type(d))
print(d)

print(d["one"], d["two"], d[3])
d["one"] = 1.0
d[4] = "4.0"
print(d)

d["one"] = "one"
print(d)

print(d.get("one"))
print(d.get("", "not found"))