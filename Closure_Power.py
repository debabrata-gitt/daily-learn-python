def power_function(power):

    def calculate(number):
        return number ** power

    return calculate


square = power_function(2)
cube = power_function(3)

print(square(4))
print(cube(4))