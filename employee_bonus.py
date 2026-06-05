class Employee:
    def calculate_bonus(self, *args):
        salary = args[0]

        if len(args) == 1:
            bonus = salary * 0.10
        elif args[1] == "Excellent":
            bonus = salary * 0.20
        elif args[1] == "Good":
            bonus = salary * 0.15
        else:
            bonus = salary * 0.05

        print("Bonus:", bonus)


emp = Employee()

emp.calculate_bonus(50000)
emp.calculate_bonus(50000, "Excellent")
emp.calculate_bonus(50000, "Good")
emp.calculate_bonus(50000, "Average")