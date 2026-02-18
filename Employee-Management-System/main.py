"""
Employee Management System
Author: Jeeva Sneha C L
Technology: Python,SQLite
Description: Console-based system to manage employee records
"""


import sqlite3

# Connect to database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()


# ==============================
# FUNCTIONS
# ==============================

def add_employee():
    print("\n--- Add Employee ---")

    name = input("Enter Name: ").strip()
    if name == "":
        print("❌ Name cannot be empty.")
        return

    department = input("Enter Department: ").strip()
    if department == "":
        print("❌ Department cannot be empty.")
        return

    while True:
        try:
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("❌ Invalid salary. Enter numbers only.")

    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                   (name, department, salary))
    conn.commit()
    print("✅ Employee added successfully!")


def view_employees():
    print("\n--- Employee List ---")
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    if not records:
        print("No employees found.")
        return

    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: {row[3]}")


def search_employee():
    print("\n--- Search Employee ---")
    name = input("Enter name to search: ").strip()

    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    records = cursor.fetchall()

    if not records:
        print("No matching employee found.")
        return

    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: {row[3]}")


def update_employee():
    print("\n--- Update Employee ---")
    emp_id = input("Enter Employee ID to update: ")

    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    record = cursor.fetchone()

    if not record:
        print("Employee not found.")
        return

    print("Leave blank to keep existing value.")

    new_name = input(f"New Name ({record[1]}): ").strip()
    new_department = input(f"New Department ({record[2]}): ").strip()

    while True:
        new_salary = input(f"New Salary ({record[3]}): ").strip()
        if new_salary == "":
            new_salary = record[3]
            break
        try:
            new_salary = float(new_salary)
            break
        except ValueError:
            print("Invalid salary. Enter numbers only.")

    if new_name == "":
        new_name = record[1]
    if new_department == "":
        new_department = record[2]

    cursor.execute("""
        UPDATE employees
        SET name=?, department=?, salary=?
        WHERE id=?
    """, (new_name, new_department, new_salary, emp_id))

    conn.commit()
    print("✅ Employee updated successfully!")


def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input("Enter Employee ID to delete: ")

    cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
    record = cursor.fetchone()

    if not record:
        print("Employee not found.")
        return

    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm == "yes":
        cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
        conn.commit()
        print("✅ Employee deleted successfully!")
    else:
        print("Deletion cancelled.")


# ==============================
# MAIN MENU LOOP
# ==============================

while True:
    print("\n==============================")
    print(" Employee Management System ")
    print("==============================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select 1-6.")

# Close connection
conn.close()


