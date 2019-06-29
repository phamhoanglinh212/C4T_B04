fvthg = ['money', 'money2', 'money3']
print(*fvthg, sep=', ')
add = input("Your new food : ")
fvthg.append(add)
print(*fvthg, sep=', ')
choose = int(input("You wanna choose : " ))
print(fvthg[choose].upper() )


