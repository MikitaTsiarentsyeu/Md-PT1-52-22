import json
import os
import pickle
import csv
# os.chdir("") # Choose your favorite folder.

l = (["Model", "Year", "Horsepower", "Engine size"], [{"Model":"80 1.6 Specs", "Year":1989, "Horsepower":69, "Engine size":"1595 cm3"},
    {"Model":"80 1.6 Specs", "Year":1993, "Horsepower":102, "Engine size":"1595 cm3"},
    {"Model":"80 1.8 Specs", "Year":1986, "Horsepower":75, "Engine size":"1781 cm3"},
    {"Model":"80 1.8 Specs", "Year":1989, "Horsepower":90, "Engine size":"1781 cm3"},
    {"Model":"80 1.8 S Specs", "Year":1986, "Horsepower":88, "Engine size":"1781 cm3"},
    {"Model":"80 1.9 E Specs", "Year":1986, "Horsepower":113, "Engine size":"1847 cm3"},
    {"Model":"80 1.9 E Quattro Specs", "Year":1986, "Horsepower":113, "Engine size":"1847 cm3"}])

# Let's serialize this tuple in several formates:
with open('csv_file1.csv', 'w', newline = '') as f:
    p = csv.writer(f)
    p.writerow(l[0])
    for j, d in enumerate(l[1]):
        str = []
        for i, e in enumerate(l[0]):
            str.append(d[l[0][i]])
        p.writerow(str)

with open("json_file1.json", 'w') as f:
    json.dump(l, f)

with open("pickle_file1.pickle", "wb") as f:
    pickle.dump(l, f)

# And now let's read what we've just writed:
with open("csv_file1.csv", "r") as f:
    r = csv.reader(f)
    str = []
    for l in r:
        str.append(l)
    l = [str[0],[str[i+1] for i in range(len(str) - 1)]]
    for n in range(len(l[1])):
        d = {}
        for i in range(len(l[0])):
            d[l[0][i]] = l[1][n][i]
        l[1][n] = d
print(f'1. \n{l}\n')

with open("json_file1.json", "r") as f:
    l = json.load(f)
print(f'2. \n{l}\n')

with open("pickle_file1.pickle", "rb") as f:
    l = pickle.load(f)
print(f'3. \n{l}\n')