s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

s = s.split()

s = sorted([{"five":5, "thirteen":13, "two": 2, "eleven":11, "seventeen": 17, "one":1, "ten":10, "four":4, "eight":8, "five":5, "nineteen":19}[s] for s in set(s)])

print(s)

s += [True, 0, 0]

print(s)

while True:

    if s[s[-1]] % 2 != 0:
        s[-2] += s[s[-1]]

    if isinstance(s[s[-1]+1], bool):
        break

    if s[-3]:
        print(f"{s[s[-1]]}*{s[s[-1]+1]} = {s[s[-1]]*s[s[-1]+1]}")
    else:
        print(f"{s[s[-1]]}+{s[s[-1]+1]} = {s[s[-1]]+s[s[-1]+1]}")

    # print(s[s[-1]])
    s[-3] = not s[-3]
    s[-1] += 1


print(f"the sum is {s[-2]}")