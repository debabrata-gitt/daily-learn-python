
from pathlib import Path

path = Path("demo.txt")

if path.is_file():
    print("File size:", path.stat().st_size, "bytes")
else:
    print("File not found!")
