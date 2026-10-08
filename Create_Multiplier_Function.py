def multiplier(x):

    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))