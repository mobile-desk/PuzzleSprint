a = input("enter a string: ").lower()
b = []

for i in a:
  if i in b:
    b.remove(i)
  else:
    b.append(i)
    
print(b[0])