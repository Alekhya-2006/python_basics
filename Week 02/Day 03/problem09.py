# create student dictionary and print all values:

stu_details = {}

stu_details["name"] =  input("enter name: ")
stu_details["age"] = int(input("enter age: "))
stu_details["course"] = input("enter course: ")

print(list(stu_details.values()))