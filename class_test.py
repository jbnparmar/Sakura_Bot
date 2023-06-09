from RelationValueManipulationFunctions import Relation

rel = Relation("json_test.json")

rel.set_rel("apple", 0.6, 8)

print(rel.get_rel())
print(rel.get_rel_value('apple'))