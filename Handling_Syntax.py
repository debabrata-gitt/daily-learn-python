try:
    code = "print('Hello'"
    compile(code, "<string>", "exec")

except SyntaxError:
    print("Syntax error found in code")