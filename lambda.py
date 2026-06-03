employee_info = lambda *args, **kwargs: print(f"Name: {args[0]}, Department: {kwargs['department']}, Salary: {kwargs['salary']}")

employee_info("Anu", department="IT", salary=65000)