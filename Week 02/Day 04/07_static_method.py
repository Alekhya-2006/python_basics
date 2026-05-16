# static method:

# no compulsory parameter

# static method cannot directly access instance (self)
# or class (cls) attributes unless passed explicitly

# decorator --> @staticmethod

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
    
    @staticmethod
    def calc_dicount(price, discount):
        final_price = price - (discount * price / 100)
        print(f'discounted price = {final_price}')

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

Laptop.calc_dicount(40_000, 10) # 40_000 = 40000 