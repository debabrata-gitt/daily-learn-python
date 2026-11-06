try:
    raise BlockingIOError("Operation would block")

except BlockingIOError as e:
    print("Error:", e)