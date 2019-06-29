things = input("Things you like : ")
things2 = things.split()
for i, item in enumerate(things2):
    print(i+1, '.', item)
