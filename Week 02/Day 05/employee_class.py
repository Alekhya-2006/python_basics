# Employee Class
# Concepts: Constructors, Objects, Instance Variables

class Employee:

    department = "Research Department"

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


    def get_details(self):

        print(
            f"\nEmployee Name : {self.name}"
            f"\nSalary : {self.salary}"
            f"\nDepartment : {self.department}"
        )


employees = []

print("Enter details of 3 employees")

for i in range(1,4):

    name = input(f"Enter employee {i} name: ")
    salary = int(input("Enter salary: "))

    emp = Employee(name, salary)

    employees.append(emp)


print("\nEmployee Details")

for emp in employees:
    emp.get_details()