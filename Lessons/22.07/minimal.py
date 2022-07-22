l = [3,2,5,3,4,7,5,9,-45]
m = 0
for i, e in enumerate(l):
    if e<l[m]:
        m = i
print(m)
m = 0
for i in range(len(l)):
    if l[i]<l[m]:
        m = i
m = 0
i = 0
while i < len(l):
    if l[i]<l[m]:
        m = i
    i += 1
print(m)
# print(min(l))


l = ["test", "cat", "go"]
m = 0
for i, e in enumerate(l):
    if len(e)<len(l[m]):
        m = i
print(m)
# print(min(l)) wrong answer