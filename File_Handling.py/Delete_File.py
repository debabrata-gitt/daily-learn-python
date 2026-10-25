
from pathlib import Path

file_path = Path("temporary.txt")

if file_path.is_file():
    file_path.unlink()
    print("File deleted!")
else:
    print("File not found.")
