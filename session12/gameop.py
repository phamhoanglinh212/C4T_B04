

M = {
    "x":4,
    "y":4,
} 
P = {
    "x":1,
    "y":2,
}
K = {
    "x":2,
    "y":1,
}
E = {
    "x":3,
    "y":2,
}
key_save = 0
while True:
    for y in range(M['y']):
        for x in range(M["x"]):
            if P['x']==x and P['y']==y:
                print("P",end=" ")
            elif K['x']==x and K['y']==y:
                if key_save == 0:
                    print("K",end=" ")
                else:
                    print("-",end=" ")
            elif E['x']==x and E['y']==y:
                print("E",end=" ")
            else:
                print("-",end =" ")
        print()
    print('-'*20)
    if P == E:
        if key_save != 0:
            print("Congratulation")
            break
        else:
            print("You must have a key to exit")
        
        
    choose = input("Move: ").upper()
    dx = 0
    dy = 0
    if choose == 'A':
        dx = -1
    elif choose == 'D':
        dx = 1
    elif choose == 'W':
        dy = -1
    elif choose == 'S':
        dy = 1
    if P['x']+dx in range(M['x']) and P['y']+dy in range(M['y']):
        P['x']+=dx
        P['y']+=dy


    if P == K:
        key_save = key_save+1
        print(key_save)
        print("You've just pick up the key")


