from pathlib import Path

def read_file(filename):
    path = Path(filename)

    try:
        with path.open("r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return "Error: File not found."

    except PermissionError:
        return "Error: Permission denied."

    except OSError as error:
        return f"File error: {error}"

filename = input("Enter filename: ")
result = read_file(filename)

print(result)