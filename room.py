from database import load_data, save_data
from validation import get_non_empty, get_integer


ROOM_FILE = "rooms.json"
STUDENT_FILE = "students.json"


def add_room():
    rooms = load_data(ROOM_FILE)

    room_number = get_non_empty("Enter Room Number: ")

    for room in rooms:
        if room["room_number"] == room_number:
            print("Room already exists.")
            return

    block = get_non_empty("Enter Block: ")
    capacity = get_integer("Enter Capacity: ", 1, 10)

    room = {
        "room_number": room_number,
        "block": block,
        "capacity": capacity,
        "occupied": 0
    }

    rooms.append(room)
    save_data(ROOM_FILE, rooms)

    print("Room added successfully.")


def view_rooms():
    rooms = load_data(ROOM_FILE)

    if not rooms:
        print("No rooms available.")
        return

    print("\n" + "=" * 70)
    print("ROOM RECORDS")
    print("=" * 70)

    for room in rooms:
        available = room["capacity"] - room["occupied"]

        print(f"Room Number : {room['room_number']}")
        print(f"Block       : {room['block']}")
        print(f"Capacity    : {room['capacity']}")
        print(f"Occupied    : {room['occupied']}")
        print(f"Available   : {available}")
        print("-" * 70)


def allocate_room():
    students = load_data(STUDENT_FILE)
    rooms = load_data(ROOM_FILE)

    student_id = get_non_empty("Enter Student ID: ")

    student = None

    for s in students:
        if s["student_id"] == student_id:
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    if student["room_number"] is not None:
        print("Student already has a room.")
        return

    room_number = get_non_empty("Enter Room Number: ")

    room = None

    for r in rooms:
        if r["room_number"] == room_number:
            room = r
            break

    if room is None:
        print("Room not found.")
        return

    if room["occupied"] >= room["capacity"]:
        print("Room is full.")
        return

    student["room_number"] = room_number
    room["occupied"] += 1

    save_data(STUDENT_FILE, students)
    save_data(ROOM_FILE, rooms)

    print("Room allocated successfully.")


def vacate_room():
    students = load_data(STUDENT_FILE)
    rooms = load_data(ROOM_FILE)

    student_id = get_non_empty("Enter Student ID: ")

    student = None

    for s in students:
        if s["student_id"] == student_id:
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    if student["room_number"] is None:
        print("Student does not have an allocated room.")
        return

    room_number = student["room_number"]

    for room in rooms:
        if room["room_number"] == room_number:
            if room["occupied"] > 0:
                room["occupied"] -= 1
            break

    student["room_number"] = None

    save_data(STUDENT_FILE, students)
    save_data(ROOM_FILE, rooms)

    print("Room vacated successfully.")


def room_menu():
    while True:
        print("\n" + "=" * 45)
        print("ROOM MANAGEMENT")
        print("=" * 45)
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Allocate Room")
        print("4. Vacate Room")
        print("5. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            allocate_room()
        elif choice == "4":
            vacate_room()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")