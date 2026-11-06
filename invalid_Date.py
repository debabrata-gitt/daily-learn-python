from datetime import datetime12

try:
    date = input("Enter date (DD-MM-YYYY): ")
    result = datetime.strptime(date, "%d-%m-%Y")

    print("Valid date:", result.date())

except ValueError:
    print("Invalid date format")