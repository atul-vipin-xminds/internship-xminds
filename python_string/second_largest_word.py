sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort(key=len)

print("Second largest word:", words[-2])