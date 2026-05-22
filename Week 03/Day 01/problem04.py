# Employee Salary System
# Concepts: Abstraction, Abstract Methods,
# Inheritance, Polymorphism

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Employee):

    def calc_salary(self):
        return 10000
    
class FullTimeEmployee(Employee):

    def calc_salary(self):
        return 50000
    
class ContractEmployee(Employee):

    def calc_salary(self):
        return 25000       
    
intern = Intern("Alekhya")
print(f'\nName : {intern.name}\n'
      f"Salary of intern = {intern.calc_salary()}")

fulltime = FullTimeEmployee("Anu")
print(f'\nName : {fulltime.name}\n'
      f"Salary of Full Time Employee = {fulltime.calc_salary()}")

contract = ContractEmployee("Ammu")
print(f'\nName : {contract.name}\n'
      f"Salary of Contract Employee = {contract.calc_salary()}")