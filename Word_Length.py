with open("data.txt", "r") as file:
    words = file.read().split()

if words:
    average = sum(len(word) for word in words) / len(words)
    print("Average word length:", round(average, 2))
else:
    print("No words found")