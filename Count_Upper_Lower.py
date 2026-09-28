def count_lower_upper(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return {
        "uppercase": upper,
        "lowercase": lower
    }
text = input("Enter a string: ")

result = count_lower_upper(text)

print("Result:", result)