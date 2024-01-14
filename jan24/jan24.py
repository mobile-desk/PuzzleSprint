change = [25, 10, 5, 1]
changeNeeded  = int(input("Enter the needed change: "))
a = 0

while changeNeeded > 0:
    for i in change:
        if changeNeeded >= i:
            changeNeeded -= i
            a += 1
            break

print(a)