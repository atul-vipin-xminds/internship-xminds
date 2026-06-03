employees = {
    101: {"name": "Rahul", "salary": 65000, "department": "IT"},
    102: {"name": "Anu", "salary": 55000, "department": "HR"},
    103: {"name": "John", "salary": 85000, "department": "IT"}
}

# Group employees by department
departments = {}

for emp_id, details in employees.items():
    dept = details["department"]

    if dept not in departments:
        departments[dept] = []

    departments[dept].append(details)

print("Employees Grouped by Department:")
for dept, emps in departments.items():
    print(dept, ":", emps)


# Count employees in each department
print("\nEmployee Count by Department:")
for dept, emps in departments.items():
    print(dept, ":", len(emps))


# Find average salary department-wise
print("\nAverage Salary by Department:")
for dept, emps in departments.items():
    total = 0

    for emp in emps:
        total += emp["salary"]

    avg = total / len(emps)
    print(dept, ":", avg)


# Function for max()
def get_salary(emp):
    return emp["salary"]


# Find highest-paid employee in each department
print("\nHighest Paid Employee by Department:")
for dept, emps in departments.items():
    highest = max(emps, key=get_salary)
    print(dept, ":", highest["name"], "-", highest["salary"])


# Function for sorted()
def salary_key(item):
    return item[1]["salary"]


# Display employees sorted by salary
print("\nEmployees Sorted by Salary:")
sorted_employees = sorted(employees.items(), key=salary_key)

for emp_id, details in sorted_employees:
    print(emp_id, details)


# Search employees by department
search_dept = input("\nEnter department to search: ")

print("Employees in", search_dept)
for emp_id, details in employees.items():
    if details["department"].lower() == search_dept.lower():
        print(emp_id, details)


# Generate department-wise salary report
print("\nDepartment-wise Salary Report")

for dept, emps in departments.items():
    total_salary = 0

    for emp in emps:
        total_salary += emp["salary"]

    avg_salary = total_salary / len(emps)

    print("\nDepartment:", dept)
    print("Total Employees:", len(emps))
    print("Total Salary:", total_salary)
    print("Average Salary:", avg_salary)