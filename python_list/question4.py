# Question 4: Take a number from the user and remove its first occurrence from the list.

numbers = [10, 20, 30, 20, 40, 50]

print("Current list:", numbers)
number_to_remove = int(input("Enter a number to remove its first occurrence: "))

if number_to_remove in numbers:
    numbers.remove(number_to_remove)
    print("Updated list:", numbers)
else:
    print("Number not found in the list.")
