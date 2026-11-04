try:
    raise ConnectionError("Unable to connect to server")

except ConnectionError as e:
    print("Connection Error:", e)