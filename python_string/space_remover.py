sentence = input("Enter a sentence: ")

result = ""
prev_space = False

for ch in sentence:
    if ch == " ":
        if not prev_space:
            result += ch
        prev_space = True
    else:
        result += ch
        prev_space = False

print("Sentence after removing extra spaces:")
print(result)