from pathlib import Path
from datetime import datetime, timedelta

folder = Path(".")
cutoff = datetime.now().timestamp() - timedelta(hours=24).total_seconds()

for file in folder.iterdir():
    if file.is_file():
        if file.stat().st_mtime >= cutoff:
            print("Recently modified:", file.name)