things = ['money1', 'money2', 'money3', 'money4', 'money5']
while True:
    
    items = ['C', 'R', 'U', 'D']
    print(*things, sep=', ')
    print("4 choices for you :", *items)

    choose = input("You wanna choose : ")
    if choose == 'C':
        add = input("What do you want to add ? ")
        things.append(add)
        print(*things, sep=', ')

    elif choose == 'R':
        length = len(things)
        if length > 0:
            for i, item in enumerate(things):
                print(i+1, '.', item)
        elif length == 0:
            print("ERROR")

    elif choose == 'U':
        update = int(input("What do you want to update ? "))
        to = input("Your food you like : ")
        things[update] = to
        print(*things, sep=', ')

    elif choose == 'D':
        delete = input("What do you want to delete ? ")
        things.remove(delete)
        print(*things, sep=', ')
        break

    else:
        print("TRY AGAIN")
        break
        


    
    




