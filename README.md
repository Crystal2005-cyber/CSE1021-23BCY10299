# 🏨 Hostel Management System

## 📌 Project Overview

The **Hostel Management System** is a Python-based application designed to simplify and organize common hostel management activities. The system provides a structured way to manage student records, room allocation, hostel fees, complaints, and generate useful reports.

The project is developed as part of the **CSE1021** course and demonstrates the practical application of Python programming concepts such as functions, conditional statements, loops, lists, dictionaries, file handling, modules, exception handling, and data validation.

The system follows a modular design so that each major hostel-management activity can be handled independently.

---

## 🎯 Objectives

The main objectives of the project are:

* To maintain student hostel records efficiently.
* To manage hostel rooms and room allocation.
* To record and track hostel fee payments.
* To manage student complaints.
* To provide hostel-related reports and summaries.
* To reduce manual record management.
* To demonstrate Python programming concepts through a practical application.
* To provide proper validation and error handling for user inputs.

---

## ✨ Features

### 1. 👨‍🎓 Student Management

The student management module allows the administrator to:

* Add a new student.
* View all registered students.
* Search for a student.
* Update student information.
* Delete student records.
* Validate student details.

### 2. 🛏️ Room Management

The room management module provides:

* Room record management.
* Display of available rooms.
* Student room allocation.
* Room vacancy management.
* Occupancy tracking.
* Room capacity validation.

### 3. 💰 Fee Management

The Fee Management module provides the following features:

* Record student fee payments
* View fee payment records
* View individual student fee history
* Calculate total fees collected
* Generate fee reports based on recorded payments

Note: The current implementation records successful payments with the status PAID. Pending fee tracking is not implemented in the current version and can be added as a future enhancement

### 4. 📝 Complaint Management

The complaint module provides:

* Complaint registration.
* Complaint viewing.
* Complaint status updates.
* Complaint resolution tracking.
* Student-wise complaint records.

### 5. 📊 Reports and Analytics

The reporting module provides:

* Student reports.
* Room occupancy reports.
* Available-room reports.
* Fee payment reports.
* Pending-fee reports.
* Complaint status reports.

---

## 🛠️ Technologies Used

| Technology               | Purpose                     |
| ------------------------ | --------------------------- |
| **Python 3**             | Main programming language   |
| **JSON**                 | Data storage                |
| **Python File Handling** | Reading and writing records |
| **Git**                  | Version control             |
| **GitHub**               | Source-code repository      |

---

## 📂 Project Structure

```text
Hostel-Management-System/
│
├── main.py
├── student.py
├── room.py
├── fees.py
├── complaints.py
├── reports.py
├── database.py
├── validation.py
├── utils.py
├── test_project.py
│
├── data/
│   ├── students.json
│   ├── rooms.json
│   ├── fees.json
│   └── complaints.json
│
├── diagrams/
│   ├── use_case_diagram.png
│   ├── workflow_diagram.png
│   ├── class_diagram.png
│   ├── sequence_diagram.png
│   └── er_diagram.png
│
├── README.md
├── statement.md
└── requirements.txt
```

---

## ⚙️ Functional Modules

The project consists of the following major functional modules:

1. **Student Management**
2. **Room Management**
3. **Fee Management**
4. **Complaint Management**
5. **Reports and Analytics**

Each module performs a specific function and communicates with the main application through defined operations.

---

## 🔄 System Workflow

```text
                    START
                      │
                      ▼
                 Main Menu
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
     Students       Rooms          Fees
        │             │             │
        ▼             ▼             ▼
     Manage        Allocate       Manage
     Records        Rooms         Payments
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
                 Complaints
                      │
                      ▼
                   Reports
                      │
                      ▼
                    EXIT
```

---

## 📋 Requirements

Before running the project, make sure the following software is installed:

* Python 3.x
* Git
* A code editor such as VS Code, PyCharm, or IDLE

No external Python libraries are required if the project uses only Python's built-in modules.

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
https://github.com/Crystal2005-cyber/CSE1021-23BCY10299.git
```

### Step 2: Open the Project Directory

```bash
cd Hostel-Management-System
```

### Step 3: Check Python Installation

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 4: Run the Application

```bash
python main.py
```

---

## 💻 Usage

After running `main.py`, the system displays the main menu.

Example:

```text
========================================
       HOSTEL MANAGEMENT SYSTEM
========================================

1. Student Management
2. Room Management
3. Fee Management
4. Complaint Management
5. Reports
6. Exit

Enter your choice:
```

The user selects an option and follows the instructions displayed by the system.

---

## 🧪 Testing

The project includes validation and testing to ensure that the major functionalities work correctly.

Testing includes:

* Adding valid student records.
* Preventing duplicate student IDs.
* Searching for existing and non-existing students.
* Updating student records.
* Deleting student records.
* Allocating available rooms.
* Preventing allocation when a room is full.
* Recording fee payments.
* Checking pending fees.
* Registering complaints.
* Updating complaint status.
* Generating reports.
* Handling invalid user input.

### Run Tests

```bash
python test_project.py
```

---

## ⚠️ Error Handling

The system handles common input and operational errors such as:

* Invalid menu choices.
* Invalid student IDs.
* Duplicate records.
* Invalid room numbers.
* Full-room allocation attempts.
* Invalid numerical values.
* Missing records.
* Invalid file/data operations.

Python exception handling is used wherever required to prevent unexpected program termination.

---

## 🔐 Non-Functional Requirements

The project considers the following non-functional requirements:

### Usability

The system uses a simple menu-driven interface so that users can easily access different functions.

### Performance

Records should be retrieved and processed efficiently for normal hostel operations.

### Reliability

The system should maintain consistent records during student, room, fee, and complaint operations.

### Maintainability

The application is divided into separate modules so individual components can be modified without affecting the entire system.

### Security

Input validation is implemented to reduce invalid or unexpected data entry.

### Error Handling

The system provides appropriate handling for invalid input and unavailable records.

---

## 📐 Design Diagrams

The project documentation contains the following diagrams:

* Use Case Diagram
* Workflow Diagram
* Class Diagram
* Sequence Diagram
* ER Diagram

The diagrams are available in the `diagrams/` directory.

---

## 📚 Python Concepts Demonstrated

This project demonstrates the practical use of:

* Variables and data types
* Input and output
* Conditional statements
* Loops
* Functions
* Lists
* Tuples
* Dictionaries
* Strings
* File handling
* Exception handling
* Modules
* Data validation
* Searching
* Sorting
* Modular programming

---

## 🔮 Future Enhancements

The following features can be added in future versions:

* Graphical User Interface (GUI)
* Database integration using MySQL or SQLite
* Admin and student login system
* Online fee payment integration
* Email/SMS notifications
* Automated room allocation
* Advanced data analytics
* Cloud-based storage
* Mobile application integration

---

## 👥 Target Users

The system is primarily designed for:

* Hostel administrators
* Hostel wardens
* Hostel management staff

It can also be extended to provide limited functionality to students.

---

## 📌 Project Information

**Project Title:** Hostel Management System
**Course:** CSE1021
**Programming Language:** Python
**Project Type:** Academic / Mini Project
**Version:** 1.0

---

## 📖 References

* Python documentation
* CSE1021 course materials
* VITyarthi Build Your Own Project guidelines
* Python programming concepts and standard library documentation

---

## 📄 License

This project is developed for **academic and educational purposes** as part of the CSE1021 course.
