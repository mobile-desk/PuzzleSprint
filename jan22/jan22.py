from random import *

a = int(input("What is the highest number the system can generate: "))
b = randint(1, a+1)


d = 3

while d > 0:
    c = int(input("Guess what the system generated: "))
    if c == b:
        print(f"Congrats, {c} is the correct answer")
        exit()
    else:
        if c > b:
            print("Your answer is too high")
            d -= 1
        else:
            print("Your answer is too low")
            d -= 1

print("Game over")