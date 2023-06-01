import json

# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

# print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

# Opening JSON file
with open('test_JSON.json', 'r') as openfile:
# Reading from json file
    json_object = json.load(openfile)
print(json_object["apple"])
print(json_object["apple"]["value"])
print(json_object["apple"]["counter"])
print(type(json_object["apple"]))
print(type(json_object))
