from random import*
import random

M = {
    "x":4,
    "y":4,
} 
P = {
    "x":randint(0,3),
    "y":randint(0,3),
}
K = {
    "x":randint(0,3),
    "y":randint(0,3),
}
E = {
    "x":randint(0,3),
    "y":randint(0,3),
}
C = {
    "x":randint(0,3),
    "y":randint(0,3),
}
D = {
    "x":randint(0,3),
    "y":randint(0,3),
}
H = {
    "x":randint(0,3),
    "y":randint(0,3),
}
R = {
    "x": randint(0,3),
    "y": randint(0,3),
}

score = 0
key_save = 0
key_save1 = 0
yourHP = 0
monster = 0

while True:
    for y in range(M['y']):
        for x in range(M["x"]):
            if P['x']==x and P['y']==y:
                print("P",end=" ")
            elif R['x']==x and R['y']==y:
                if monster == 0:
                    print("-",end=" ")
                else:
                    print("H", end=" ")
            elif K['x']==x and K['y']==y:
                if key_save < 1:
                    print("K",end=" ")
                else:
                    print("-",end=" ")
            elif E['x']==x and E['y']==y:
                print("E",end=" ")
            elif H['x']==x and H['y']==y:
                print("-",end=" ")
            elif C['x']==x and C["y"]==y:
                if key_save1 < 1:
                    print("C", end=" ")
                else:
                    print("-", end=" ")
            elif D['x']==x and D['y']==y:
                if score == 0:
                    print("D", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("-",end =" ")
        print()
    print('-'*20)

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
        print("You've just pick up the key")

    if P == C:
        key_save1 +=1
        print("You've just pick up the key")

    if P == D:
        score +=100
        print("Yup, you've eaten diamond")
        print("Điểm hiện tại: ", score)

    if P == H:
        yourHP += 1
        print("You are so fucking lucky. Số mạng của bạn: ", yourHP )
        print("*****************")

    if P == R:
        may = ["búa", "kéo", "lá"]
        may2 = random.choice(may)
        print("Vào ô monster")
        choose_mon = input("Đánh hay chạy: ")
        while True:
            if choose_mon == "đánh":
                tancong = input("Lá, búa hay kéo: ")
                if tancong == "búa" and may2 == "kéo":
                    print("Máy: ", may2)
                    print("You win")
                    monster +=1
                    break
                elif tancong == "búa" and may2 == "lá":
                    print("Máy: ", may2)
                    print("You lose")
                    score -=1000
                    print("Điểm hiện tại: ", score)
                    break
                elif tancong == "lá" and may2 == "búa":
                    print("Máy: ", may2)
                    print("You win")
                    monster +=1
                    break
                elif tancong == "lá" and may2 == "kéo":
                    print("Máy: ", may2)
                    print("You lose")
                    score -=1000
                    print("Điểm hiện tại: ", score)
                    break
                elif tancong == "kéo" and may2 == "lá":
                    print("Máy: ", may2)
                    print("You win")
                    monster +=1
                    break
                elif tancong == "kéo" and may2 == "búa":
                    print("Máy: ", may2)
                    print("You lose")
                    score -=1000
                    print("Điểm hiện tại: ", score)
                    break
                elif tancong == may2:
                    print("Máy: ", may2)
                    print("Hòa. Play again")
            if choose_mon == "chạy":
                if yourHP > 0:
                    print("Bạn có:", yourHP, "mạng. Bạn được thoát")
                    monster += 1
                    break
                elif yourHP == 0:
                    print("Bạn chưa nhặt được mạng nào. Không thể chạy")
                    tancong = input("Lá, búa hay kéo: ")
                    if tancong == "búa" and may2 == "kéo":
                        print("Máy: ", may2)
                        print("You win")
                        monster +=1
                        break
                    elif tancong == "búa" and may2 == "lá":
                        print("Máy: ", may2)
                        print("You lose")
                        score -=1000
                        print("Điểm hiện tại: ", score)
                        break
                    elif tancong == "lá" and may2 == "búa":
                        print("Máy: ", may2)
                        print("You win")
                        monster +=1
                        break
                    elif tancong == "lá" and may2 == "kéo":
                        print("Máy: ", may2)
                        print("You lose")
                        score -=1000
                        print("Điểm hiện tại: ", score)
                        break
                    elif tancong == "kéo" and may2 == "lá":
                        print("Máy: ", may2)
                        print("You win")
                        monster +=1
                        break
                    elif tancong == "kéo" and may2 == "búa":
                        print("Máy: ", may2)
                        print("You lose")
                        score -=1000
                        print("Điểm hiện tại: ", score)
                        break
                    elif tancong == may2:
                        print("Máy: ", may2)
                        print("Hòa. Play again")
                    
                
        

    if P == E:
        sum = key_save + key_save1
        if sum >= 2:
            print("Congratulation")
            print("Your total score: ", score)
            break
        else:
            print("You must have 2 key to exit")
        






