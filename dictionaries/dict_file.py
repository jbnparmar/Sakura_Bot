import json

f = open("dict_txt.json", "r")

dict1 = json.loads(f.read())

print(dict1["apple"])

print(dict1["apple"]["value"])
print(dict1["apple"]["count"])

dict2 = { "banana": { "value": 3, "count": 5} }

dict1.update(dict2)

print(dict1)

with open("dict_txt.json", "w") as outfile:
    outfile.write(json.dumps(dict1))

print(dict1)