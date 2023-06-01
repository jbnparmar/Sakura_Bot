import json

def import_test():
    print("Imported Successfully!!!")

def get_relation_table():
    """returns file text to avoid problems, when file name changes"""
    with open("balde_de_relacoes.json", "r") as file:
        rel = json.load(file)
    return rel

def get_rel_initial_value(name):
    rel = get_relation_table()
    return rel[name]["value"]

def get_rel_count(name):
    rel = get_relation_table()
    return rel[name]["count"]

def get_rel_value(name):
    value = float(get_rel_initial_value(name)/get_rel_count(name))
    return value