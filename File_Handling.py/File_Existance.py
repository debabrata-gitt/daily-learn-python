
from pathlib import Path

path = Path("demo.txt")

if path.exists():
    print("File exists!")
else:
    print("File does not exist.")
