def make_adder(number):
    def add(value):
        return number + value

    return add


add10 = make_adder(10)
add20 = make_adder(20)

print(add10(5))
print(add20(5))