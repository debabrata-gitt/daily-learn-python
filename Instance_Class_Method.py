class Temperature:
    unit = "Celsius"

    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value, self.unit)

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit


t1 = Temperature(25)
t1.show()

Temperature.change_unit("Degree C")
t1.show()