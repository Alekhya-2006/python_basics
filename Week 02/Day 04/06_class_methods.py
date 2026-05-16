# class method:
# 1st parameter --> cls
# can access class attributes but can't access instance attributes
# decorator --> @classmethod
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod    
    def get_storage_type(cls):
        print(f'storage type = {cls.storage_type}')

    def get_info(self): # instance method
        print(f'laptop has {self.RAM} RAM and {self.storage} {self.storage_type}')
        # can access the class and instance parameters

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

Laptop.get_storage_type()