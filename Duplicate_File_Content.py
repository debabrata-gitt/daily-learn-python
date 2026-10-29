from pathlib import Path
import hashlib

folder = Path(".")

file_hashes = {}

for file in folder.iterdir():
    if file.is_file():
        try:
            with open(file, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()

            if file_hash in file_hashes:
                print("Duplicate:", file.name)
                print("Same as:", file_hashes[file_hash])
            else:
                file_hashes[file_hash] = file.name

        except OSError as error:
            print("Could not read", file.name, error)