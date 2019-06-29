color = ['pink', 'green', 'blue', 'red', 'black']
print(*color, sep=', ')
# color.remove('pink')
# print(*color, sep=', ')
choose = input("letter or number :")
print(choose)
if choose == "number":
    delete1 = int(input("The number you choose : "))
    color.pop(delete1)
    print(*color, sep=', ')

elif choose == "letter":
    delete2 = input("The color you choose : ")
    color.remove(delete2)
    print(*color, sep=', ')
    