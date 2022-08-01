chunk = 10000000

with open("", "rb") as donor:
    with open("", "wb") as receiver:
        count = 0
        while True:
            c = donor.read(chunk)
            if c:
                receiver.write(c)
                count += 1
                print(count)
            else:
                break
        print("done!")

# with open("", "rb") as f: NOT OPTIMAL
#     data = f.read()

# with open("", "wb") as f:
#     f.write(data)
#     print("done!")

