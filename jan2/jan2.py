import re
s = re.sub(r'^a-zA-Z0-9', '', input("Enter word here: ").lower())

if s == s[::-1]:
    print("True")
else:
    print("False")