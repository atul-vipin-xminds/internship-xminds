# Question 7: Count how many times a number appears in a list.

numbers = [1, 2, 3, 2, 4, 2, 5, 2]

print("Current list:", numbers)
target = int(input("Enter the number to count: "))

count = numbers.count(target)

print("No of times the number appears in the list:", count)
