dict1 = { "apple": { "value": 2, "count": 3} }
dict2 = { "banana": { "value": 5, "count": 4} }

print(dict1)
print(dict1["apple"]["value"])
print(dict1["apple"]["count"])
print()
print(dict2)
print(dict2["banana"]["value"])
print(dict2["banana"]["count"])

dict1.update(dict2)

print(dict1)