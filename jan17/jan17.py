b = [1,5,7,11,2,0]
a = ['q','w','e','r','t','y']


n = len(a)
for i in range(n):
  for j in range(0, n-i-1):
    if a[j] > a[j+1]:
      a[j], a[j+1] = a[j+1], a[j]


print(a)
