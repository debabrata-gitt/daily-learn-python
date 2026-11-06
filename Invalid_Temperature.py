class TemperatureError(Exception):
    pass

try:
    temp = float(input("Enter temperature: "))

    if temp < -273.15:
        raise TemperatureError("Temperature cannot be below absolute zero")

    print("Valid temperature:", temp)

except ValueError:
    print("Enter a valid number")

except TemperatureError as e:
    print(e)