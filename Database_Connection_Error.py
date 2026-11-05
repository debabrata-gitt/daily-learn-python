try:
    raise ConnectionError("Database connection failed")

except ConnectionError as e:
    print("Database Error:", e)

finally:
    print("Database operation completed")