# Create a dictionary as following using nested dictionary.
# Find employee by ID.
# Add a new employee.
# Update salary.
# Delete an employee.
# Display all employees.

employees = {
    101: {
        "name": "Rahul",
        "salary": 65000
    },
    102: {
        "name": "Anu",
        "salary": 55000
    }
}

# Find employee by ID
employee_id = int(input("Enter employee ID to find: "))
print("Employee details:", employees[employee_id])

# Add a new employee
new_id = int(input("Enter new employee ID: "))
new_name = input("Enter employee name: ")
new_salary = int(input("Enter employee salary: "))
employees[new_id] = {"name": new_name, "salary": new_salary}

# Update salary
update_id = int(input("Enter employee ID to update salary: "))
updated_salary = int(input("Enter new salary: "))
employees[update_id]["salary"] = updated_salary

# Delete an employee
delete_id = int(input("Enter employee ID to delete: "))
del employees[delete_id]

# Display all employees
print("All employees:")
for emp_id, details in employees.items():
    print(emp_id, details)
