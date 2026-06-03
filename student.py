def student_performance(*marks, passing_mark=40, **student):
    print("Student Name :", student.get("name"))
    print("Student ID   :", student.get("id"))

    total = sum(marks)
    average = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    passed = 0
    failed = 0

    for mark in marks:
        if mark >= passing_mark:
            passed += 1
        else:
            failed += 1

    result = "Pass" if failed == 0 else "Fail"

    print("Total Marks      :", total)
    print("Average Marks    :", average)
    print("Highest Mark     :", highest)
    print("Lowest Mark      :", lowest)
    print("Subjects Passed  :", passed)
    print("Subjects Failed  :", failed)
    print("Final Result     :", result)


student_performance(
    75, 82, 90, 65, 38,
    name="Atul",
    id=101
)