players = {
    "Player1": 120,
    "Player2": 250,
    "Player3": 180,
    "Player4": 300
}

ranking = sorted(players.items(), key=lambda x: x[1], reverse=True)

print("🏆 SCOREBOARD")

for position, (name, score) in enumerate(ranking, 1):
    print(position, name, "-", score)