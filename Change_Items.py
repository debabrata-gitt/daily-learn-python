class Numbers:
    def __init__(self):
        self.data = [10, 20, 30]

    def __setitem__(self, index, value):
        self.data[index] = value

n = Numbers()

n[1] = 100

print(n.data)