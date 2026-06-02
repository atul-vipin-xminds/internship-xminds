# Question 6: Find the index of a given element.

elements = [12, 25, 37, 48, 59, 25]

print("Current list:", elements)
target = int(input("Enter the element to find its index: "))

if target in elements:
    print("Index of the element:", elements.index(target))
else:
    print("Element not found in the list.")
