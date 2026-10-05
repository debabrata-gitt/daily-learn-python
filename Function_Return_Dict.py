def student(name, marks):
    return {
        "name": name,
        "marks": marks,
        "passed": marks >= 40
    }


result = student("Rahul", 85)
print(result)