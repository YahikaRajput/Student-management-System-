# Student Management System
students = []
def add_students():
    print("\n---Add Student---")
    name = input("Enter  name: ")
    roll = input("Enter  roll number: ")
    marks = input("Enter  marks: ")

    students.append([name, roll, marks])
    print("Student Added Succcessfully!\n ")

def display_students():
    print("\n---Students Records---")
    if len(students) == 0:
        print("No  records found.\n")
    else:
        print("Name\tRoll\tMarks")
        print("-----------------------")
        for s in students:
            print(s[0],"\t ", s[1], "\t", s[2])
        print()

#search student
def search_students():
    print("\n---Search student---")
    roll = input("Enter roll number : ")
    found = False

    for s in students:
        if s[1] == roll:
            print("Student found: ")
            print("Name :", s[0])
            print("Marks:", s[2], "\n")
            found = True
            break
        if not found:
            print("Student not found.\n")

# delete student
def delete_student():
    print("\n---Delete student---")
    roll = input("Enter roll number: ")
    found = False
    
    for s in students:
        if s[1]== roll:
            students.remove(s)
            print("Students deleted successfully!\n")
            found = True
            break
        if not found:
            print("Student not found\n")


# main program
while True:
    print("=====Student Management System====")
    print("1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_students()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_students()
    elif choice == '4':
        print("Exit..")
    elif choice == '5':
        print("Thank you for using the system!")
    else:
        print("Invalid choice, try again.\n")

