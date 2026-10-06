def remove_spaces(text):

    if text == "":
        return ""

    if text[0] == " ":
        return remove_spaces(text[1:])

    return text[0] + remove_spaces(text[1:])


print(remove_spaces("Python is very powerful"))