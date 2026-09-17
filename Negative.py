class Number:
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return -self.value

n = Number(10)

print(-n)