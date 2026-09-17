class Number:
    def __init__(self, value):
        self.value = value

    def __pow__(self, other):
        return self.value ** other.value

a = Number(2)
b = Number(3)

print(a ** b)