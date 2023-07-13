from RelationValueManipulationFunctions import *

rel = Relation("json_test.json")

# print(rel.get_rel("apple"))

rel.add_rel("banana", 0.1, 6)

# print(rel.get_rel("banana"))

print(rel.get_bucket())

rel.add_rel("cat", 0.12, 14)

print(rel.get_bucket())