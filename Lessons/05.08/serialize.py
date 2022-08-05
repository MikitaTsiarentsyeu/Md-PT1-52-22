import csv
import json
import pickle

json_example = '{"width":3840,"height":2100,"resolution":90,"quality":90,"settings":[{"filename":"_largePreview1.jpg","seek":10},{"filename":"_largePreview2.jpg","seek":35},{"filename":"_largePreview3.jpg","seek":70},{"filename":"_largePreview4.jpg","seek":95}]}'

data = json.loads(json_example)
print(type(data), data)

data["width"] += 0.1

print(data["settings"])
data["settings"] = tuple(data["settings"])
print(data["settings"])

new_ex = json.dumps(data)
print(type(new_ex), new_ex)

data = json.loads(json_example)
print(type(data["settings"]), data["settings"])

data["settings"] = tuple(data["settings"])

new_pckl = pickle.dumps(data)
print(new_pckl)

data = pickle.loads(new_pckl)
print(data, type(data))

new_pckl = pickle.dumps(print)
new_print = pickle.loads(new_pckl)
new_print("test", "my", "new", "print")

new_new_print = print
new_new_print("test", "my", "new", "print")

with open("test.pickle", 'wb') as f:
    pickle.dump(data, f)

with open("test.json", 'w') as f:
    json.dump(data, f)

with open("test.pickle", 'rb') as f:
    print(pickle.load(f))

with open("test.json", 'r') as f:
    print(json.load(f))

keys = ["engine size","model", "year", "horsepower"]
data_v1 = {"model":["80 1.6 Specs", "80 1.6 Specs"], "year":[1989, 1993], "horsepower":[69, 102], "engine size":[1595, 1595]}

data_v2 = [
    {"model":"80 1.6 Specs", "year":1989, "horsepower":69, "engine size":1595},
    {"model":"80 1.6 Specs", "year":1993, "horsepower":102, "engine size":1595}
]

with open("v2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for line in data_v2:
        # writer.writerow(line.values())
        row = []
        for key in keys:
            row.append(line[key])
        writer.writerow(row)


with open("v1.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for i in range(len(data_v1[keys[0]])):
        row = []
        for key in keys:
            row.append(data_v1[key][i])
        writer.writerow(row)


with open("v1.json", 'w', newline='') as f:
    json.dump(data_v1, f)

with open("v2.json", 'w', newline='') as f:
    json.dump(data_v2, f)

with open("v1.pickle", 'wb') as f:
    pickle.dump(data_v1, f)

with open("v2.pickle", 'wb') as f:
    pickle.dump(data_v2, f)