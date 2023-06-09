from RelationValueManipulationFunctions import Relation

rel = Relation("json_test.json")

rel.set_rel_name("banana", 0.2, 5)

rel.set_rel_name("apple", 0.6, 8)

print(rel.get_rel_name())
print(type(rel.get_rel_name()))