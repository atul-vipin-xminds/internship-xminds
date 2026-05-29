name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
marks = float(input("Enter your marks (out of 100): "))
if marks >= 40:
    status = "Pass"
else:
    status = "Fail"
print("----- Student Details -----")
print("Name   :", name)
print("Age    :", age)
print("Course :", course)
print("Marks  :", marks)
print("Status :", status)
