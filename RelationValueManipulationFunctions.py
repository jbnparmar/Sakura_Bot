import json

def import_test():
    print("Imported Successfully!!!")

class Relation:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.dict = ""
        with open(self.bucket_name, "a") as f:
            self.dict 

