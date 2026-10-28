from pathlib import Path
from datetime import datetime
import shutil

source = Path("data.txt")

if source.is_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = Path(f"data_backup_{timestamp}.txt")

    shutil.copy2(source, backup)

    print("Backup created:", backup.name)
else:
    print("Source file does not exist.")