# Question 2: Take two lists from the user and merge them using extend().

list1 = input("Enter the elements of the first list separated by spaces: ").split()
list2 = input("Enter the elements of the second list separated by spaces: ").split()

list1.extend(list2)

print("Merged list:", list1)
