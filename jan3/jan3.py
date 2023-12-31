position = [0,0]
possible_moves = {
    "l" : -1,
    "r" : 1,
    "u" : 1,
    "d" : -1,
}

moves = input("What moves would you like to make: ").lower()

for i in moves:
    if i in possible_moves:
        if i == "l" or i == "r":
            position[0] += possible_moves[i]
        elif i == "u" or i == "d":
            position[1] += possible_moves[i]
        else:
            pass
    else:
        print(f"{i} is an invalid input")
        
print(position)
if position == [0,0]:
    print("True")
else:
    print("False")
