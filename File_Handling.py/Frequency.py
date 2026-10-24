
from collections import Counter

with open("demo.txt", "r") as file:
    words = file.read().lower().split()

frequency = Counter(words)

for word, count in frequency.items():
    print(word, ":", count)
