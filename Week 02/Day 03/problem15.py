# merge two dictionaries

dict1 = {
    "name": "Alekhya",
    "age": 20
} 

dict2 = {
    "marks" : 98,
    "branch": "CS"
}
# student = dict1 | dict2
# print(student)

dict1.update(dict2)
print(dict1)