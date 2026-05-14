# Student Marks Management System

student_marks = {}


while True:

    print("\n===== Student Marks System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student Marks")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Choose an option (1-6): "))


    # Add Student
    if choice == 1:

        name = input("enter student name: ")
        if name in student_marks:
            print("Student already exists")
        else:
            marks = int(input("enter marks: "))
            student_marks[name] = marks    

            print("Student Added successfully")

    # view all students
    elif choice == 2:
        if len(student_marks) == 0:
            print("No student record found")

        else:
            print("\nStudent Records:") 

            for name, marks in student_marks.items():
                print(f'{name} = {marks}')

    # Search Student marks               
    elif choice == 3:
        if len(student_marks) == 0:
            print("No Student record found")

        else:
            name = input("enter name of Student: ")
            if name in student_marks.keys():
                print(student_marks[name])    

            else:
                print("Student Doesn't exists")

    # update marks
    elif choice == 4:
        if len(student_marks) == 0:
            print("No Student record found")

        else:
            name = input("enter name of Student: ")
            if name in student_marks.keys():
                marks = int(input("enter the marks of the Student: "))
                student_marks[name] = marks   
                print("Marks updation Successful") 

            else:
                print("Student Doesn't exists")
                 
    # Delete Student
    elif choice == 5:
        if len(student_marks) == 0:
            print("No Student record found")

        else:
            name = input("enter student name: ") 

            if name in student_marks.keys():
                student_marks.pop(name)   
                print("Successfully deleted")

            else: 
                print("student doesn't exists")

    # Exit
    elif choice == 6:
        print("Successfully exited")
        break

    else:
        print("Invalid choice")
        print("\nchoose the correct")