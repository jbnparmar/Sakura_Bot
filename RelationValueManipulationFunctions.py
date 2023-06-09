import json

def import_test():
    print("Imported Successfully!!!")

class Relation:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        open(self.bucket_name, "w")
        self.rel_obj = []

    def set_rel(self, rel_name, value, count):
        dict = { rel_name: { "value": value, "count": count} }
        self.rel_obj.append(dict)
        with open(self.bucket_name, "a") as fp:
            json.dump(self.rel_obj, fp, indent=4, separators=(',', ': '))

    def get_rel(self):
        with open(self.bucket_name, "r") as fp:
            rel = json.load(fp)
        return rel
    
    def get_rel_value(self, rel_name):
        with open(self.bucket_name, "r") as fp:
            rel = json.load(fp)
        return rel