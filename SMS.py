students = []  # List to store student records

def show_menu():
    print("\nWelcome to the School Management System!")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Update Student Information")
    print("5. Search Student by Name or Grade")
    print("6. Sort Students by Grade")
    print("7. View Total Students")
    print("8. Exit")

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    age = input("Enter student age: ")
    students.append({"Name": name, "Grade": grade, "Age": age})
    print(f"Student {name} added successfully!")

def view_students():
    if not students:
        print("No students in the system.")
    else:
        print("\nStudent Records:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['Name']}, Grade: {student['Grade']}, Age: {student['Age']}")

def remove_student():
    view_students()
    if students:
        try:
            student_no = int(input("Enter the number of the student to remove: "))
            if 1 <= student_no <= len(students):
                removed = students.pop(student_no - 1)
                print(f"Student {removed['Name']} removed successfully!")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_student():
    view_students()
    if students:
        try:
            student_no = int(input("Enter the number of the student to update: "))
            if 1 <= student_no <= len(students):
                student = students[student_no - 1]
                print(f"Updating information for {student['Name']}")
                student['Name'] = input(f"Enter new name (current: {student['Name']}): ")
                student['Grade'] = input(f"Enter new grade (current: {student['Grade']}): ")
                student['Age'] = input(f"Enter new age (current: {student['Age']}): ")
                print(f"Student {student['Name']} updated successfully!")
            else:
                print("Invalid student number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def search_student():
    search_term = input("Enter name or grade to search: ").lower()
    found_students = [student for student in students if search_term in student['Name'].lower() or search_term in student['Grade'].lower()]
    if found_students:
        print("\nSearch Results:")
        for student in found_students:
            print(f"Name: {student['Name']}, Grade: {student['Grade']}, Age: {student['Age']}")
    else:
        print("No students found matching your search.")

def sort_students():
    students.sort(key=lambda student: student['Grade'])
    print("Students sorted by grade.")

def view_total_students():
    print(f"\nTotal number of students: {len(students)}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            view_total_students()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()