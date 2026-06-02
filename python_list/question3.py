# Question 3: Create a list of names and insert a new name at a position specified by the user.

names = ["Aman", "Neha", "Ravi", "Priya"]

print("Current names:", names)
new_name = input("Enter the new name to insert: ")
position = int(input("Enter the position to insert : "))

names.insert(position, new_name)

print("Updated names list:", names)
