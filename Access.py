class Numbers:
    def __init__(self):
        self.data = [10, 20, 30, 40]

    def __getitem__(self, index):
        return self.data[index]

n = Numbers()

print(n[0])
print(n[2])