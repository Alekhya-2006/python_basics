# JSON Module --> JavaScript Object Notation
import json

# json to python

json_str = '{"name": "Alekhya", "age": 20, "isStudent": true, "Backlogs": null}'

py_obj = json.loads(json_str)
print(type(py_obj), py_obj) # dict

# python to json

python_object = {
    "Name": "Teena",
    "Age": 21,
    "isStudent" : True,
    "Backlogs": None
}

json_string = json.dumps(python_object)
print(type(json_string),json_string)