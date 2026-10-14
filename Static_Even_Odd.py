class Number:
    @staticmethod
    def check_even(number):
        return number % 2 == 0


print(Number.check_even(12))
print(Number.check_even(7))