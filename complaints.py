from database import load_data, save_data
from validation import get_non_empty


FILE = "complaints.json"
STUDENT_FILE = "students.json"


def register_complaint():
    complaints = load_data(FILE)
    students = load_data(STUDENT_FILE)

    student_id = get_non_empty("Enter Student ID: ")

    if not any(s["student_id"] == student_id for s in students):
        print("Student not found.")
        return

    complaint_id = get_non_empty("Enter Complaint ID: ")

    if any(c["complaint_id"] == complaint_id for c in complaints):
        print("Complaint ID already exists.")
        return

    category = get_non_empty("Enter Category: ")
    description = get_non_empty("Enter Complaint Description: ")

    complaint = {
        "complaint_id": complaint_id,
        "student_id": student_id,
        "category": category,
        "description": description,
        "status": "OPEN"
    }

    complaints.append(complaint)
    save_data(FILE, complaints)

    print("Complaint registered successfully.")


def view_complaints():
    complaints = load_data(FILE)

    if not complaints:
        print("No complaints found.")
        return

    print("\n" + "=" * 75)
    print("COMPLAINT RECORDS")
    print("=" * 75)

    for complaint in complaints:
        print(f"Complaint ID : {complaint['complaint_id']}")
        print(f"Student ID   : {complaint['student_id']}")
        print(f"Category     : {complaint['category']}")
        print(f"Description  : {complaint['description']}")
        print(f"Status       : {complaint['status']}")
        print("-" * 75)


def update_complaint():
    complaints = load_data(FILE)

    complaint_id = get_non_empty("Enter Complaint ID: ")

    for complaint in complaints:
        if complaint["complaint_id"] == complaint_id:

            print("1. OPEN")
            print("2. IN PROGRESS")
            print("3. RESOLVED")

            choice = input("Select status: ").strip()

            statuses = {
                "1": "OPEN",
                "2": "IN PROGRESS",
                "3": "RESOLVED"
            }

            if choice not in statuses:
                print("Invalid status.")
                return

            complaint["status"] = statuses[choice]

            save_data(FILE, complaints)

            print("Complaint status updated.")
            return

    print("Complaint not found.")


def complaint_menu():
    while True:
        print("\n" + "=" * 45)
        print("COMPLAINT MANAGEMENT")
        print("=" * 45)
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Update Complaint")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_complaint()
        elif choice == "2":
            view_complaints()
        elif choice == "3":
            update_complaint()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")