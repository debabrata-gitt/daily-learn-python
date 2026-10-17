from collections import Counter

fruits = ["apple", "mango", "apple", "orange",
          "mango", "apple"]

result = Counter(fruits)

print(result)
print("Apple count:", result["apple"])
print("Most common:", result.most_common(1))