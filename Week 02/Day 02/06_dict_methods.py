# dictionary methods

stu_details = {
    "name" : "Alekhya",
    "gpa" : 8.2,
    "subjects" : ["maths", "computer networks", "OS"],
    3.14 :"PI"
}

d_keys = list(stu_details.keys()) # returns all keys
print(d_keys) 
print(type(d_keys)) # list

d_vals = stu_details.values() # returns all values
print(d_vals)
print(type(d_vals)) #  type is "dict_values"

d_items = stu_details.items() # returns( key , val) pairs
print(d_items)
print(type(d_items)) # dict_items

# stu_details["age"] --> error since age key is not in the dict
print(stu_details.get("age")) # no error but shows None

stu_details.update({
    "age" : 20
})
print(stu_details)