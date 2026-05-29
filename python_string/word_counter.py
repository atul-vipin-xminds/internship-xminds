sentence = "Python C Java Python C++ Python PHP"

words = sentence.split()

max_count = 0
most_word = ""

for word in set(words):
    count = words.count(word)
    if count > max_count:
        max_count = count
        most_word = word

print("Most repeated word:", most_word)
print("Count:", max_count)