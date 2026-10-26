from collections import Counter

with open("data.txt", "r") as file:
    text = file.read().lower()

words = text.split()
word_count = Counter(words)

if word_count:
    word, count = word_count.most_common(1)[0]
    print("Most frequent word:", word)
    print("Frequency:", count)
else:
    print("The file is empty.")