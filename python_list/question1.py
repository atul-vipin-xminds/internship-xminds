# Question 1: Create an empty list and ask the user to enter 5 numbers. Store them using append() and display the list.

numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

print("List of numbers:", numbers)
