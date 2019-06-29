fvthg = ['money 1', 'money 2', 'money 3']
print(*fvthg, sep=', ')
change = int(input("You wanna change : "))
to = input("Your food you like : ")
fvthg[change] = to
print(*fvthg, sep=', ')