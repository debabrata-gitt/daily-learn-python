from pathlib import Path

folder = Path(".")
search_name = input("Enter filename to search: ")

found = False

for path in folder.rglob("*"):
    if path.is_file() and path.name == search_name:
        print("File found:", path.resolve())
        found = True

if not found:
    print("File not found.")