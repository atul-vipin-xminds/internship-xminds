# Question 1: Add new members
members = {"atul", "varun", "alwin", "adith"}
print("Current members:", members)
new_member = input("Enter the name of the new member: ")
members.add(new_member)
print("Updated members:", members)

# Question 2: Display all members
print("All library members:")
for member in members:
    print(member)

# Question 3: Remove a specific member
member_to_remove = input("Enter the member name to remove: ")
members.remove(member_to_remove)
print("Members after removal:", members)


# Question 4: Find common members between two libraries
library1 = set(input("Enter members of library 1: ").split(","))
library2 = set(input("Enter members of library 2: ").split(","))
common_members = library1.intersection(library2)
print("Common members:", common_members)

# Question 5: Merge members in two libraries
library3 = set(input("Enter members of another library separated by spaces: ").split())
library4 = set(input("Enter members of one more library separated by spaces: ").split())
merged_members = library3.union(library4)
print("Merged members:", merged_members)
