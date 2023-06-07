import json

def import_test():
    print("Imported Successfully!!!")

class Relation():
    def __init__(self, happiness_bucket):
        self.rel = open(happiness_bucket, "a+")
        self.name = ""
        self.value = 0.0
        self.count = 0.0

    def set_rel_name(self, name):
        self.name = name
        self.rel.writelines(self.name)