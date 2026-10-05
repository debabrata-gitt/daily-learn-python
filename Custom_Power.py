def make_power(exponent):
    def calculate(number):
        return number ** exponent

    return calculate


square = make_power(2)
cube = make_power(3)

print(square(5))
print(cube(5))