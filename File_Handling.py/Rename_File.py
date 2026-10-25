
from pathlib import Path

old = Path("old.txt")
new = Path("new.txt")

if old.is_file():
    old.rename(new)
    print("File renamed!")
else:
    print("Original file not found.")
