def anagram(a, b):
    return sorted(a) == sorted(b)

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if anagram(word1, word2):
    print("Anagram")
else:
    print("Not Anagram")