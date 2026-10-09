words = [
    "cat",
    "python",
    "computer",
    "AI",
    "programming"
]

result = list(
    filter(lambda word: len(word) > 5, words)
)

print(result)