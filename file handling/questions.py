#question1
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#question2
file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    content = file.read()

words = content.split()
print("Number of words:", len(words))

#question3
import random

file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    content = file.read()

random_position = random.randint(0, len(content) - 1)

with open(file_name, "r") as file:
    file.seek(random_position)
    data = file.read()

print("Random position:", random_position)
print("Data from that position:")
print(data)