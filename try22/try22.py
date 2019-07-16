from random import*
M = {
    'x':5,
    'y':5,
}
P = {
    'x': randint(0,3),
    'y': randint(0,3),
}
K = {
    'x': randint(0,3),
    'y': randint(0,3),
}
E = {
    'x': randint(0,3),
    'y': randint(0,3),
}
K2 = {
    'x': randint(0,3),
    'y':randint(0,3),
}
key = 0
while True:
    for y in range(M['y']):
        for x in range(M['x']):
            if P['x'] == x and P['y'] == y:
                print('P', end='')
            elif K['x'] == x and K['y'] == y:
                if key < 1:
                    print('K', end='')
                elif key == 1:
                    print('-', end='')
            elif K2['x'] == x and K['y'] == y:
                if key < 2:
                    print('K', end='')
                elif key == 1:
                print('K2', end='')
            elif E['x'] == x and E['y'] == y:
                print('E', end='')
            else:
                print('-', end='')
        print()
    dx = 0
    dy = 0
    choose = input("Your move: ").upper()
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
    if K == P:
        key +=1
        print("You have a key")
    if P == E:
        if key == 0:
            print('You must take the key')
        else:
            print("You out")
            break
