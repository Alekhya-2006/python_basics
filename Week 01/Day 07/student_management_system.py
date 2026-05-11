# Student Management System

students = []

while True:

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    n = int(input("choose what you wanna do now(1-5): "))
    
    if n == 5:
        print("Exit successful")
        break
    
    if n >= 1 and n <= 4:

        if n == 1:       
            name = input("enter name: ")
            age = int(input("enter age: "))
            students.append([name, age])
            print("added successfully")

        elif n == 2:
            if len(students) == 0:
                print("No students found")

            else:    
                for i in range(len(students)):
                    print(i, students[i])

        elif n == 3:
            if len(students) == 0:
                print("no students")
                

            else:    
                student_id = int(input("enter the id of the student: ")) # index = id
            
                if student_id >= 0 and student_id < len(students):
                    print(students[student_id])
                
                else:
                    print("invalid student Id") 
            

        else:

            if len(students) == 0:
                print("No students")

            else:

                student_id = int(input("enter the id of the student: "))

                if student_id >= 0 and student_id < len(students):
                    students.pop(student_id)
                    print("deleted successfully")

                else:
                    print("invalid student Id")
    else:
        print("Choose the correct option.")            