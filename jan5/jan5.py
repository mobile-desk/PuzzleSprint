a = [3, 1, 2, 4, 6, 5, 7, 8]

even = []
odd = []

for i in a:
  if i % 2 == 0:
    even.append(i)
  else:
     odd.append(i)
     
  
  
b = even + odd
print(b)