from pathlib import Path

file = Path("notes.txt")

if file.exists():
    print("File exists")
else:
    print("File does not exist")