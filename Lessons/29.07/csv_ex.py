import csv

fieldnames = ["sku","make","model","color"]

with open("test.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)
    writer.writerow(["4535636","adidas","superstar","black"])
    writer.writerows([["4535647","nike","air max","white"], ["4345636","puma","suede","blue"]])

with open("test.csv", 'r', newline='') as f:
    reader = csv.reader(f)
    for l in reader:
        print(repr(l))
        for elem in l:
            print(elem)

with open("test.csv", 'r', newline='') as f:
    lines = f.readlines()
    for l in lines:
        l = l.split(',')
        print(repr(l))
        for elem in l:
            print(repr(elem))

with open("test.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerow({fieldnames[0]:"4535636",fieldnames[1]:"adidas",fieldnames[2]:"superstar",fieldnames[3]:"black"})

with open("test.csv", 'r', newline='') as f:
    reader = csv.DictReader(f)
    for l in reader:
        print(repr(l))