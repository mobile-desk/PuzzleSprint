number = int(input("Enter number: "))
limit = int(input("Enter limit: "))

for i in range(1, limit+1):
  print(f"{number} * {i} = {number*i}")