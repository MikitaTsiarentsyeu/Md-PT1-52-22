s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
d = {"five": 5,"thirteen": 13, "two": 2, "eleven":11, "seventeen": 17, "three": 3,"one": 1, "nine":9, "ten":10 ,"four":4 ,"eight": 8 , "six": 6, "nineteen":19, "seven": 7, "twelve":12, "fourteen":14, "fithteen":15, "sixteen":16, "eighteen": 18}

l = list({d[x] for x in s.split()})


for i in range (len(l)-1):
    if i%2 == 0:
        print (f"multiplication: {l[i]*l[(i+1)]}")
    else:
        print (f" sum: {l[i]+l[(i+1)]}")

odd = [l[i] for l[i] in list(l) if  l[i] % 2 !=0 ]

print(f"The sum  of odd elements is {sum(odd)}")