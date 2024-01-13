def totalLegs(chickens, cows, pigs):
  chickens *= 2
  cows *= 4
  pigs *= 4
  return chickens + cows + pigs

pigs = int(input("How many pigs are present: "))
cows = int(input("How many cows are present: "))
chickens = int(input("How many chickens are present: "))
print(totalLegs(chickens, cows, pigs))
  
