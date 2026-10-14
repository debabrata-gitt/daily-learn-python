class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def compare(self, other):
        if self.score > other.score:
            return self.name + " wins"
        elif self.score < other.score:
            return other.name + " wins"
        return "Draw"


p1 = Player("Rahul", 90)
p2 = Player("Amit", 85)

print(p1.compare(p2))