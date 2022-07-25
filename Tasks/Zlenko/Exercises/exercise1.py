s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
d = {"five": 5, "thirteen": 13, "two": 2, "eleven": 11, 
"seventeen": 17, "two": 2, "one": 1, "thirteen": 13, "ten": 10, 
"four": 4, "eight": 8, "five": 5, "nineteen": 19} 
l = list({d[x] for x in s.split()})
print(l)
for i in range (len(l)-1):  
    if i%2 == 0:
        print (l[i]*l[(i+1)])
    else:
        print (l[i]+l[(i+1)])
total = 0
for x in l:
    if x%2 == 1:
        total = total + x
print(f"The sum of odd numbers is: {total}")