# a list of tuples with info(name, subject)
# list all unique courses
# list students enrolled in English
# create dic(student, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
# list all unique courses
s = set()
for tup in info:
    s.add(tup[1])

print("Subjects =", list(s))

# Students enrolled in english
print("\nStudents enrolled in english:")

for tup in info:
    
    if tup[1] == "English":
        print(tup[0])    

# create dict(students --> set of courses)

details = {}

for tup in info:

    name = tup[0]
    subject = tup[1]

    if name not in details:
        details[name] = set()

    details[name].add(subject)    
    
print("\nStudent Details:")
print(details)