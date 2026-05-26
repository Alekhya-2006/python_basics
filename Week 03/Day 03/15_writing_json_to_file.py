import json

data = {
    "name": "Laxmi",
    "age": 42,
    "isStudent": False
}

with open("data.json", "w") as f:
    json.dump(data, f, indent = 4, sort_keys = True)