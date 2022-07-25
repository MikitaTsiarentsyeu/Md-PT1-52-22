l = [x for x in range(1, 11)]
print(l)

# l = []
# for x in range(1, 11):
#     l.append(x)


l = [str(x)*x for x in range(1, 11)]
print(l)

# l = []
# for x in range(1, 11):
#     l.append(str(x)*x)


l = [1,2,3,4,5,6,7,8,9,10]

print([x+100 for x in l])

print([x+100 for x in l if x > 3])
# l = []
# for x in range(1, 11):
#     if x > 3:
#         l.append(str(x)*x)

print([x+100 for x in l if x > 30])

print([x+100 for x in l if x > 3 if x < 9])
l = []
for x in range(1, 11):
    if x > 3:
        if x < 9:
            l.append(str(x)*x)


print([x+100 if x%2==0 else x*100 for x in range(1,11) if x > 3])

l1 = [1,2,3,4,5,6,7,8]
l2 = [0,1,2,3]
print([x**y for x in l1 for y in l2])
print([f"{x}-{y}" for x in l1 for y in l2])

l = []
for x in l1:
    for y in l2:
        l.append(x**y)

l = [[1,2,3], [4,5,6], [7,8,9]]
print([y for x in l for y in x])

d = {"zero":0, "one":1}
print([f"{k}:{v}" for k, v in d.items()])

print({x:str(x) for x in range(10)})