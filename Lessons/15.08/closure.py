def print_ad(text):
    def inner(times):
        print((text*times).capitalize())
    return inner

print_short_text = print_ad("some very short ad")
print_long_text = print_ad("soooomeeeeee veeeeeryyyyyyy llooooooooong teeeeeeext")

# print_short_text(5)

# print_long_text(3)


def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

c1 = counter(10)
c2 = counter(120)
c3 = counter(555)

for i in range(10):
    print(c1(), c2(), c3())