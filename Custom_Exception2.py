class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    print("Valid marks:", marks)

except ValueError:
    print("Enter numeric marks")

except InvalidMarksError as e:
    print(e)