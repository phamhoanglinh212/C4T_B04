quan = ['CG', 'DD', 'TH', 'BTL', 'NTL']
km = [117.43, 9.224, 43.35, 12.04, 9.96]
population = [150.300, 247.100, 333.300, 266.800, 420.900]
mdd =[]
for (a, b) in zip(population, km):
    mdds = a //b
    mdd.append(mdds)
mdd.sort()
for (a, b,c) in zip(population, km,mdd):
    print(c) 

tb = sum(mdd) // len(quan)
print("mddc tb : ", tb)









