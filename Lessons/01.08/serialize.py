import json

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



