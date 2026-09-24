from database import initialize_data
from student import student_menu
from room import room_menu
from fees import fee_menu
from complaints import complaint_menu
from reports import reports_menu


def main():
    initialize_data()

    while True:
        print("\n")
        print("=" * 60)
        print("             HOSTEL MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Student Management")
        print("2. Room Management")
        print("3. Fee Management")
        print("4. Complaint Management")
        print("5. Reports and Analytics")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            student_menu()

        elif choice == "2":
            room_menu()

        elif choice == "3":
            fee_menu()

        elif choice == "4":
            complaint_menu()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("\nThank you for using Hostel Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()