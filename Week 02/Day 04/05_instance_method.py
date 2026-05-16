# instance method:
# 1st parameter --> self, which is compulsory

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self): # instance method
        print(f'laptop has {self.RAM} RAM and {self.storage} {self.storage_type}')
        # can access the class and instance parameters

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()