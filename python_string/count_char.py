word = input("Enter a word: ")

freq = {}

for ch in word.lower():
    freq[ch] = freq.get(ch, 0) + 1

for ch, count in freq.items():
    print(ch, ":", count)