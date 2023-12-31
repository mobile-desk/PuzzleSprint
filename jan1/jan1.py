list = [2,7,11,15]
target = 9


for i in list:
    for j in list:
        if i != j:
            if i + j == target:
                total = [list.index(i), list.index(j)]
                print(total)
                break