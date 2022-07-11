x = 0

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")


if x >= 0:
    print("positive")
else:
    print("negative")


print("positive") if x >= 0 else print("negative")

print("positive" if x >= 0 else "negative")

print("positive") if x > 0 else print("zero") if x == 0 else print("negative")

x = "positive" if x >= 0 else "negative"
print(x)



