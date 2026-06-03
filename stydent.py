def student_report(*args, **kwargs):
    total = sum(args)
    average = (lambda marks: sum(marks) / len(marks))(args)

    print("Student Name :", kwargs["name"])
    print("Roll Number  :", kwargs["roll_no"])
    print("Total Marks  :", total)
    print("Average Marks:", average)

student_report(85, 90, 78, 88, name="Anu", roll_no=101)