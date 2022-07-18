d = {1:"one", 2:"two"}
print(d[1], d[2])
# d[3] error
print(d.get(3, "not found"))
print(d.get(2, "not found"))

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print(list(d))

# del d[1]
# d.pop(1)
print(d.popitem())
print(d)


s = {1,2,3}
print(type(s), s)

s = set()
print(type(s), s)

l = [1,2,3,3,4,4,5,6,7]
print(set(l))
l = list(set(l))
print(l)

s = "rrffddsstyhh"
print(set(s))
s = ''.join(set(s))
print(s)


l1 = [1,2,3]
l2 = [3,2,1,3]
print(l1 == l2)
print(set(l1) == set(l2))

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))
print({1,2,3}.issubset({1,2,3,4}))
print({1,2,3,4}.issuperset({1,2,3}))

# {1,2,3,[]} error

s = {1,2,3}
s.add(3)
s.add(4)
print(s)

s.update([4,5,6,7])
print(s)

# print(s[0]) error

s.remove(7)
print(s)

# s.remove(7)
s.discard(7)
print(s)

s = set("test")
print(s.pop(), s)
print(s.pop(), s)
print(s.pop(), s)

s.clear()
print(s)



l = [[1,2,3], [4,5,6], [7,8,9]]
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

print(l[0:2][0][0])

t = (l, "test")
print(t[0])
t[0][0][0] = 1.0
print(t)
print(l)

d = {(1,2,3): "one two three"}
# d = {t:"test"} error
d = {"test":t}

set(t)