# Question 1: Store student details in a tuple and display it using loop.
student_details = (
    ("101", "alwin", 20, "BSc Computer Science"),
    ("102", "varun", 21, "BCom"),
    ("103", "abhi", 19, "BCA"),
)

print("Student details:")
for student in student_details:
    for detail in student:
        print(detail)
    print()

# Question 2: Store marks of a student in a tuple and slice the tuple to print
# 2.1 first three scores
# 2.2 last two scores
# 2.3 middle scores
marks = (78, 85, 92, 88, 76, 95)

print("All scores:", marks)
print("First three scores:", marks[:3])
print("Last two scores:", marks[-2:])
print("Middle scores:", marks[1:-1])

# Question 3: In a tuple of student names count how many times a specific name appears.
student_names = ("atul", "varun", "alwin", "adith", "lino", "abhi")

name_to_count = input("Enter the name to count: ")
count = student_names.count(name_to_count)

print(f"{name_to_count} appears {count} time(s) in the tuple.")

# Question 5: From the nested tuple, display all employees and perform different operations.
employees = (
    (101, "Rahul", "Developer", 65000),
    (102, "Anu", "Tester", 55000),
    (103, "John", "Manager", 85000)
)

# Display all employees
print("All employees:")
for employee in employees:
    print(employee)

# Find employee by ID
search_id = int(input("Enter employee ID to search: "))
for employee in employees:
    if employee[0] == search_id:
        print("Employee found by ID:", employee)

# Count employees in a designation
designation = input("Enter designation to count: ")
designation_count = 0
for employee in employees:
    if employee[2].lower() == designation.lower():
        designation_count += 1
print("Number of employees in designation:", designation_count)

# Find highest salary
salary_list = []
for employee in employees:
    salary_list.append(employee[3])

highest_salary = max(salary_list)
print("Highest salary:", highest_salary)

# Find lowest salary
lowest_salary = min(salary_list)
print("Lowest salary:", lowest_salary)

# Calculate average salary
total_salary = sum(salary_list)
average_salary = total_salary / len(employees)
print("Average salary:", average_salary)

# Search employee name
search_name = input("Enter employee name to search: ")
for employee in employees:
    if employee[1].lower() == search_name.lower():
        print("Employee found by name:", employee)

# Display employees earning above 60000
print("Employees earning above 60000:")
for employee in employees:
    if employee[3] > 60000:
        print(employee)

# Sort by salary (convert to list first)
employee_list = list(employees)
employee_list.sort(key=lambda employee: employee[3])
print("Employees sorted by salary:", employee_list)

# Unpack employee details and display them
print("Unpacked employee details:")
for emp_id, name, job, salary in employees:
    print("ID:", emp_id, "Name:", name, "Designation:", job, "Salary:", salary)
