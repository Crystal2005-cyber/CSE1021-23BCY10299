from database import load_data, save_data
from validation import get_non_empty, get_float


FILE = "fees.json"
STUDENT_FILE = "students.json"


def record_payment():
    fees = load_data(FILE)
    students = load_data(STUDENT_FILE)

    student_id = get_non_empty("Enter Student ID: ")

    if not any(s["student_id"] == student_id for s in students):
        print("Student not found.")
        return

    payment_id = get_non_empty("Enter Payment ID: ")

    if any(p["payment_id"] == payment_id for p in fees):
        print("Payment ID already exists.")
        return

    amount = get_float("Enter Amount: ", 0)

    payment = {
        "payment_id": payment_id,
        "student_id": student_id,
        "amount": amount,
        "status": "PAID"
    }

    fees.append(payment)
    save_data(FILE, fees)

    print("Payment recorded successfully.")


def view_fees():
    fees = load_data(FILE)

    if not fees:
        print("No fee records found.")
        return

    print("\n" + "=" * 60)
    print("FEE RECORDS")
    print("=" * 60)

    for payment in fees:
        print(f"Payment ID : {payment['payment_id']}")
        print(f"Student ID : {payment['student_id']}")
        print(f"Amount     : ₹{payment['amount']:.2f}")
        print(f"Status     : {payment['status']}")
        print("-" * 60)


def student_fee_history():
    fees = load_data(FILE)

    student_id = get_non_empty("Enter Student ID: ")

    records = [
        payment for payment in fees
        if payment["student_id"] == student_id
    ]

    if not records:
        print("No fee records found.")
        return

    total = 0

    print("\nFee History")
    print("-" * 50)

    for payment in records:
        print(
            f"{payment['payment_id']} | "
            f"₹{payment['amount']:.2f} | "
            f"{payment['status']}"
        )

        total += payment["amount"]

    print("-" * 50)
    print(f"Total Paid: ₹{total:.2f}")


def fee_menu():
    while True:
        print("\n" + "=" * 45)
        print("FEE MANAGEMENT")
        print("=" * 45)
        print("1. Record Payment")
        print("2. View Fee Records")
        print("3. Student Fee History")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            record_payment()
        elif choice == "2":
            view_fees()
        elif choice == "3":
            student_fee_history()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")