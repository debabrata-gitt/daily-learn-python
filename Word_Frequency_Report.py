from collections import Counter
import re

with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = re.findall(r"\b\w+\b", text)
frequency = Counter(words)

with open("word_report.txt", "w", encoding="utf-8") as file:
    for word, count in frequency.most_common():
        file.write(f"{word}: {count}\n")

print("Word frequency report created!")