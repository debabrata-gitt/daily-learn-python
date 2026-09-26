def count_words(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter sentence: ")

print("Number of words:", count_words(text))