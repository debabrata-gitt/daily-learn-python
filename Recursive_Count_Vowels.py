def count_vowels(text):

    if text == "":
        return 0

    count = 1 if text[0].lower() in "aeiou" else 0

    return count + count_vowels(text[1:])


print(count_vowels("Hello Python"))