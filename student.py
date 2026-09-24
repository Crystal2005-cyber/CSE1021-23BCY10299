from database import load_data, save_data
from validation import get_non_empty, get_integer


FILE = "students.json"


def add_student():
    students = load_data(FILE)

    student_id = get_non_empty("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists.")
            return

    name = get_non_empty("Enter Student Name: ")
    age = get_integer("Enter Age: ", 15, 100)
    gender = get_non_empty("Enter Gender: ")
    course = get_non_empty("Enter Course: ")
    year = get_integer("Enter Year: ", 1, 6)
    phone = get_non_empty("Enter Phone Number: ")

    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "year": year,
        "phone": phone,
        "room_number": None
    }

    students.append(student)
    save_data(FILE, students)

    print("Student added successfully.")


def view_students():
    students = load_data(FILE)

    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 80)
    print("STUDENT RECORDS")
    print("=" * 80)

    for student in students:
        print(f"Student ID : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Gender     : {student['gender']}")
        print(f"Course     : {student['course']}")
        print(f"Year       : {student['year']}")
        print(f"Phone      : {student['phone']}")
        print(f"Room       : {student['room_number']}")
        print("-" * 80)


def search_student():
    students = load_data(FILE)

    student_id = get_non_empty("Enter Student ID to search: ")

    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent Found")
            print("-" * 40)

            for key, value in student.items():
                print(f"{key.title():15}: {value}")

            return

    print("Student not found.")


def update_student():
    students = load_data(FILE)

    student_id = get_non_empty("Enter Student ID to update: ")

    for student in students:
        if student["student_id"] == student_id:

            print("Enter new details:")

            student["name"] = get_non_empty("Name: ")
            student["age"] = get_integer("Age: ", 15, 100)
            student["gender"] = get_non_empty("Gender: ")
            student["course"] = get_non_empty("Course: ")
            student["year"] = get_integer("Year: ", 1, 6)
            student["phone"] = get_non_empty("Phone: ")

            save_data(FILE, students)

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    students = load_data(FILE)

    student_id = get_non_empty("Enter Student ID to delete: ")

    for student in students:
        if student["student_id"] == student_id:

            if student["room_number"] is not None:
                print("Cannot delete a student who is currently allocated a room.")
                return

            students.remove(student)
            save_data(FILE, students)

            print("Student deleted successfully.")
            return

    print("Student not found.")


def student_menu():
    while True:
        print("\n" + "=" * 45)
        print("STUDENT MANAGEMENT")
        print("=" * 45)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")