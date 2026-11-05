try:
    raise TimeoutError("Server response timed out")

except TimeoutError as e:
    print(e)