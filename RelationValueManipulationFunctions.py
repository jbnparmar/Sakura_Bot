import json

def import_test():
    print("Imported Successfully!!!")

class Relation():
    def __init__(self, happiness_bucket):
        self.happiness_bucket = happiness_bucket
        self.odj = []
        open(self.happiness_bucket, "w")
        self.name = ""
        self.value = 0.0
        self.count = 0.0

    def set_rel_name(self, name, value, count):
        self.name = name
        self.value = value
        self.count = count
        self.odj.append({ self.name: { "value": self.value, "count": self.count}})
        with open(self.happiness_bucket, "w") as f:
            json.dump(self.odj, f, indent=4, separators=(',', ': '))
            f.seek(0)

    def get_rel_name(self):
        with open(self.happiness_bucket, "r") as f:
            temp_bucket = json.load(f)
        return temp_bucket