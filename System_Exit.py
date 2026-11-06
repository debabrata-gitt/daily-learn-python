try:
    raise SystemExit("Program is exiting")

except SystemExit as e:
    print(e)