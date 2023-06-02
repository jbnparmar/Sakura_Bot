import json

def import_test():
    print("Imported Successfully!!!")

def get_relation_table():
    """returns file text to avoid problems, when file name changes"""
    try:
        with open("balde_de_relacoes.json", "r") as file:
            rel = json.load(file)
        return rel
    except FileNotFoundError as fnfe:
        print("\n\n" + f"!!! ERROR Relation bucket file missing { fnfe } !!!")

def get_rel_initial_value(name):
    try:
        rel = get_relation_table()
        return rel[name]["value"]
    except (KeyError, TypeError) as e:
        print("\n\n!!!ERROR get_rel_initial_value(name) !!!")
        print("Entered relation doesn't exists in the relation bucket")
        print(e)

def get_rel_count(name):
    try:
        rel = get_relation_table()
        return rel[name]["count"]
    except (KeyError, TypeError) as e:
        print("\n\n!!!ERROR get_rel_count(name) !!!")
        print("Entered relation doesn't exists in the relation bucket")
        print(e)

def get_rel_value(name):
    try:
        value = float(get_rel_initial_value(name)/get_rel_count(name))
        return value
    except TypeError as te:
        print("\n\n!!!ERROR get_rel_value(name) !!!")
        print("Entered relation doesn't exists in the relation bucket")
        print(te)
