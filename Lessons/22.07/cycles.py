# while True: will repeat infinetly
#     print("to infity and beyond!")

x = 0
while x<=10:
    print(x)
    x+=1

x = -10
while x<=0:
    print(x)
    x+=1


l = [1,2,3,4,5,6,7,8,9.0,"test"]
for my_new_variable_crated_specifically_for_the_iteration in l:
    print(my_new_variable_crated_specifically_for_the_iteration)

print(my_new_variable_crated_specifically_for_the_iteration)

for i in tuple(l):
    print(i)

for i in set("some string"):
    print(i)

d = {1:"one", 2:"two", 3:"three"}
for i in d:
    print(i)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)


for i in l:
    # l.append(i)
    print(i)
    print(l.pop())
    print(l)


for i in range(10):
    print(i)

for i in range(len(l)):
    print(l[i])

for i in range(1,10,3):
    print(i)

for i, e in enumerate("some string"):
    print(i, e)

for i in "some string":
    if i == "i":
        break
    if i == " ":
        continue
    print(i)
else:
    print("everything is fine...")


flag = True

while True:
    if not flag:
        x += 1
        flag = not flag
        continue
    print(x)
    x += 1
    flag = not flag
    if x >= 11:
        break


iterator_obj = iter(l)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
# print(next(iterator_obj)) StopIteration error

l = [[1,2,3], [4,5,6], [7,8,9]]
for i, e in enumerate(l):
    print(f"{i+1} line:")
    for j in e:
        print(j)