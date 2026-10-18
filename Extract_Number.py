import re
text = "My roll is 09 and my marks is 80."
numbers = re.findall(r"\d+", text)
print (numbers)