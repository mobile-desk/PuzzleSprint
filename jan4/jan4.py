a = input("Input string: ")

b = []

for i in a:
    if i in b:
        print(len(b))
        break
    else:
        b.append(i)