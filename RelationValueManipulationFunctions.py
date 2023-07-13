import json

def import_test():
    print("Imported Successfully!!!")

class Relation:
    def __init__(self, bucket_name):
        """Relation class can only read from existing file
            to use file for the first time, create empty file
            and {} this inside that file and just use following method to add relations
            >>> add_rel()
        """
        self.bucket_name = bucket_name
        self.dict = ""
        with open(self.bucket_name, "r") as f:
            self.dict = json.loads(f.read())

    def get_bucket(self):
        return self.dict

    def get_rel(self, rel):
        return self.dict[rel]

    def add_rel(self, rel_name, rel_value, rel_count):
        """Method an also be used to update value and count of any relation"""
        with open(self.bucket_name, "w") as f:
            dict_to_be_added = { rel_name: { "value": rel_value, "count": rel_count } }
            self.dict.update(dict_to_be_added)
            f.write(json.dumps(self.dict))