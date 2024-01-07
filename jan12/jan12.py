from itertools import combinations

a = [-1, 0, 1, 2, -1, -4]

result = []

# Generate all combinations of 3 elements from the list 'a'
comb = combinations(a, 3)

# Check combinations that sum up to zero and store them in 'result'
for c in comb:
    if sum(c) == 0:
        c = list(c)
        c.sort()
        if c in result:
          pass
        else:
          result.append(list(c))

print(result)