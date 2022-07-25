s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

d = {"five":5, "thirteen":13, "two": 2, "eleven":11, "seventeen": 17, "one":1, "ten":10, "four":4, "eight":8, "five":5, "nineteen":19}

l = list({d[x] for x in s.split()})
print(l)
