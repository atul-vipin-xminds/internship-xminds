# Question 8: Create a copy of a list and modify the copied list. Verify that the original list remains unchanged.

original_list = [10, 20, 30, 40]
copied_list = original_list.copy()

print("Original list before modification:", original_list)
print("Copied list before modification:", copied_list)

copied_list.append(50)
copied_list[0] = 99

print("Original list after copied list modification:", original_list)
print("Modified copied list:", copied_list)
