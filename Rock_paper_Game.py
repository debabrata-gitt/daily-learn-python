import random

choices = ["rock", "paper", "scissors"]

print("===== ROCK PAPER SCISSORS =====")

player = input("Choose rock, paper, or scissors: ").lower()

if player not in choices:
    print("Invalid choice!")
else:
    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a DRAW! 🤝")

    elif (
        (player == "rock" and computer == "scissors")
        or
        (player == "paper" and computer == "rock")
        or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You WIN!")

    else:
        print("😢 You LOSE!")