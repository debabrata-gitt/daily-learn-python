class Team:
    def __init__(self):
        self.players = ["Rahul", "Amit", "Rohit"]

    def __contains__(self, name):
        return name in self.players

team = Team()

print("Rahul" in team)
print("Sohan" in team)