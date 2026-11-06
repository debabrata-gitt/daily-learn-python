try:
    raise BrokenPipeError("Pipe connection broken")

except BrokenPipeError as e:
    print("Error:", e)