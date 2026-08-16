score = 0

print("===== PYTHON QUIZ =====")

answer = input("1. Which keyword is used to define a function? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("2. What is the output of 2 + 3? ")

if answer == "5":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("3. Which symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour score:", score, "/ 3")