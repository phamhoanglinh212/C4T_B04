things = []
n = int(input("Ban muon nhap ?: "))
for i in range(n):
    add = int(input("Numbers you wanna add : "))
    things.append(add)
print("Your list : ")
print(*things, sep=', ')
sum = 0
for i in things:
    sum = sum + i
print("Your result : ", sum)


