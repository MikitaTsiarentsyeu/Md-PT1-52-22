# f = open("test.txt", 'w')
# print(f)
# f.write("some new data")
# f.close()

# f.write("more of the data") error

with open("test.txt", 'w') as f:
    f.write("some data\n")
    f.write("more of the test data\n")
    f.writelines(["line 1\n", "line 2\n", "line 3"])
    # f.read()

with open("test.txt", 'r') as f:
    for line in f:
        print(repr(line))

    # lines = f.readlines()

    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # f.write("") error

    # print(f.read())
    # f.seek(15)
    # print(f.read(15))
    # print(f.read())

# with open("new_test.txt", 'w') as f:
#     f.writelines(lines)

with open("test.txt", 'a') as f:
    f.write("\nsome data from append\n")
    f.seek(0)
    f.write("prepended content\n")

with open("test.txt", 'a+') as f:
    f.write("\nappended contet from a+\n")
    f.seek(0)
    print(f.readline())
    f.write("prepended content from a+\n")

with open("test.txt", 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write("test read+ content")

with open("test.txt", 'w+') as f:
    f.write("totally new data from w+")
    f.seek(0)
    print(f.read())
    f.write("after seek")
    print(f.read())