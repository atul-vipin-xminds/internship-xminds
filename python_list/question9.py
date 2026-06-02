# Question 9: Create a list that contains employee data: employee id, name, salary, skills he knows (list type). Access the data and add another skill.

employee = [101, "Atul", 55000, ["Python", "Excel", "Communication"]]

print("Employee data:")
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])
print("Skills:", employee[3])

new_skill = input("Enter a new skill to add: ")
employee[3].append(new_skill)

print("Updated employee data:", employee)
