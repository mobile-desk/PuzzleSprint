m = int(input("Enter an integer: "))
n = m
factorial = 1

if m == 0:
  print("0! = 1")
  quit()
  
else:
  while m > 0:
    factorial *= m
    m -= 1
    
    
    
print(f"{n}! = {factorial}")