from database import load_data


def hostel_summary():
    students = load_data("students.json")
    rooms = load_data("rooms.json")
    fees = load_data("fees.json")
    complaints = load_data("complaints.json")

    total_capacity = sum(room["capacity"] for room in rooms)
    occupied = sum(room["occupied"] for room in rooms)
    available = total_capacity - occupied

    total_fees = sum(payment["amount"] for payment in fees)

    open_complaints = sum(
        1 for complaint in complaints
        if complaint["status"] != "RESOLVED"
    )

    print("\n" + "=" * 60)
    print("HOSTEL SUMMARY REPORT")
    print("=" * 60)

    print(f"Total Students      : {len(students)}")
    print(f"Total Rooms         : {len(rooms)}")
    print(f"Total Capacity      : {total_capacity}")
    print(f"Occupied Beds       : {occupied}")
    print(f"Available Beds      : {available}")
    print(f"Total Fees Collected: ₹{total_fees:.2f}")
    print(f"Pending Complaints  : {open_complaints}")

    print("=" * 60)


def room_report():
    rooms = load_data("rooms.json")

    print("\nROOM AVAILABILITY REPORT")
    print("-" * 60)

    for room in rooms:
        available = room["capacity"] - room["occupied"]

        print(
            f"Room {room['room_number']} | "
            f"Capacity: {room['capacity']} | "
            f"Occupied: {room['occupied']} | "
            f"Available: {available}"
        )


def fee_report():
    fees = load_data("fees.json")

    print("\nFEE REPORT")
    print("-" * 60)

    if not fees:
        print("No fee records found.")
        return

    student_totals = {}

    for payment in fees:
        student_id = payment["student_id"]

        if student_id not in student_totals:
            student_totals[student_id] = 0

        student_totals[student_id] += payment["amount"]

    for student_id, total in student_totals.items():
        print(f"{student_id}: ₹{total:.2f}")


def complaint_report():
    complaints = load_data("complaints.json")

    print("\nCOMPLAINT REPORT")
    print("-" * 60)

    open_count = 0
    progress_count = 0
    resolved_count = 0

    for complaint in complaints:
        if complaint["status"] == "OPEN":
            open_count += 1
        elif complaint["status"] == "IN PROGRESS":
            progress_count += 1
        elif complaint["status"] == "RESOLVED":
            resolved_count += 1

    print(f"Open Complaints       : {open_count}")
    print(f"In Progress Complaints: {progress_count}")
    print(f"Resolved Complaints   : {resolved_count}")


def reports_menu():
    while True:
        print("\n" + "=" * 45)
        print("REPORTS")
        print("=" * 45)
        print("1. Hostel Summary")
        print("2. Room Report")
        print("3. Fee Report")
        print("4. Complaint Report")
        print("5. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            hostel_summary()
        elif choice == "2":
            room_report()
        elif choice == "3":
            fee_report()
        elif choice == "4":
            complaint_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")