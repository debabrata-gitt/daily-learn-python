words = ["apple", "ant", "banana", "ball", "cat"]

result = {}

for word in words:
    first = word[0]

    if first not in result:
        result[first] = []

    result[first].append(word)

print(result)