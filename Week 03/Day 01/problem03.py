# Vehicle Management System
# Concepts: Inheritance, super(), Constructors

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


c1 = Car("BMW", "M76", 4)

print(f'\nBrand = {c1.brand}'
      f'\nModel = {c1.model}'
      f'\nNumber of Seats = {c1.seats}')

b1 = Bike("Vespa", "D12", 125)

print(f'\nBrand = {b1.brand}'
      f'\nModel = {b1.model}'
      f'\nEngine CC = {b1.engine_cc}')