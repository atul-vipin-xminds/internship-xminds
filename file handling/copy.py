file1 = input("Enter the input file name: ")
file2 = input("Enter the output file name: ")

with open(file1, "r") as source:
    content = source.read()

with open(file2, "w") as target:
    target.write(content)

print("Content copied successfully.")