# 1. Define a Student class with the following attributes: name, roll_number, marks.
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_no}, Marks: {self.marks}"

# 2. List to Store Students:    
students = []

# 3. Add Students:
def add_student():
    while True:
        try:
            name = input("Enter student name: ")
            roll_no = int(input("Enter roll number: "))
            marks = float(input("Enter marks: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for roll number and marks.")

    new_student = Student(name, roll_no, marks)
    students.append(new_student)
    print("Student added successfully.")

# 4. View All Students:
def view_all_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)

# 5. Search for a student
def search_student():
    roll_no = input("Enter the roll number to search: ")
    for student in students:
        if student.roll_no == roll_no:
            print(student)
            return
    print("Student not found.")

# 6. Update student
def update_student():
    roll_no = int(input("Enter roll number to update: "))
    updated_student = None

    for student in students:
        if student.roll_no == roll_no:
            updated_student = student
            break

    if not updated_student:
        print("Student with roll number", roll_no, "not found.")
        return

    new_name = input("Enter new name: ")
    new_marks = float(input("Enter new marks: "))

    updated_student.name = new_name
    updated_student.marks = new_marks

    print("Student information updated successfully.")

# 7. Delete student
def delete_student():
    roll_no = int(input("Enter roll number to delete: "))
    removed_student = None

    for student in students:
        if student.roll_no == roll_no:
            removed_student = student
            students.remove(student)
            break

    if not removed_student:
        print("Student with roll number", roll_no, "not found.")
    else:
        print("Student deleted successfully.")

# to return the marks of the student
def get_marks(students):
    return students.marks

def main():
    while True:
        print("\nStudent Management System")
        print("------------------------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Sort Students by Marks")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()


        elif choice == 6:
            sorted_students = sorted(students, key=get_marks, reverse=True)
            for student in sorted_students:
                print(student)
            
        elif choice == 7:
            print("You're exited from LMS...")

        else:
            print("Invalid choice. Please enter a valid option (1-7).")


if __name__ == "__main__":
    main()