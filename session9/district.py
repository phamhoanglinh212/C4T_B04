import itertools
quan = ['CG', 'DD', 'TH', 'BTL', 'NTL']
km = [117.43, 9.224, 43.35, 12.04, 9.96]
population = [150.300, 247.100, 333.300, 266.800, 420.900]
for (a, b, c) in zip(quan, km, population):
    print(a,b,c) 
print("Max population : ", max(population))
print("Min population : ", min(population))
max1 = max(population)
min1 = min(population)
for(a, b) in zip(quan, population) :
    if b == max1:
        print(a,"co so dan cao nhat")
    elif b == min1:
        print(a, "co dan so nho nhat")
        
