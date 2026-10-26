import shutil

source = "data.txt"
backup = "data_backup.txt"

try:
    shutil.copy2(source, backup)
    print("Backup created successfully!")
except FileNotFoundError:
    print("Source file not found.")
except OSError as error:
    print("Error:", error)