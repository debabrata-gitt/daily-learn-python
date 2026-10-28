from pathlib import Path

folder = Path(".")
extension_count = {}

for file in folder.iterdir():
    if file.is_file():
        extension = file.suffix.lower() or "[no extension]"
        extension_count[extension] = extension_count.get(extension, 0) + 1

for extension, count in sorted(extension_count.items()):
    print(extension, ":", count)