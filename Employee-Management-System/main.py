"""
Employee Management System
Author: Jeeva Sneha C L
Technology: Python,SQLite
Description: Console-based system to manage employee records
"""

import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL
)
""")

conn.commit()

def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
                   (name, age, department, salary))
    conn.commit()
    print("Employee added successfully!\n")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    if not rows:
        print("No employees found.\n")
    else:
        for row in rows:
            print(row)
    print()

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    department = input("Enter New Department: ")
    salary = float(input("Enter New Salary: "))

    cursor.execute("""
    UPDATE employees
    SET name=?, age=?, department=?, salary=?
    WHERE id=?
    """, (name, age, department, salary, emp_id))

    conn.commit()
    print("Employee updated successfully!\n")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    print("Employee deleted successfully!\n")

while True:
    print("===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")

conn.close()
