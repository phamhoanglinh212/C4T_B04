things = ['money 1', 'money 2', 'money 3']
print(*things, sep=', ')
delete1 = input("You wanna delete : ")
#things.pop(delete1)
things.remove(delete1)
print(*things, sep=', ')