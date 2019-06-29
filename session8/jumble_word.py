from random import *
while True:
    things = ['crush', 'dungeon', 'dracula', 'luxury', 'honey']
    word = random.choice(things)
    split = list(word)
    shuffle(split)
    print(split)
    print("Shuffle : ", *split, sep='  ')
    word2 = input("Your answer : ")
    if word2 in things:
        print("Đúng rồi nhé ^^")
        print("*"*20)
    else:
        print("Sai rồi nhé ^^")
        print("*"*20)
    conti = input("Bạn muốn chơi nữa hông ^^ ?(y/n): ").upper()
    if conti == "N":
        print("Tạm biệt nhé ^^ ahihi")
        break
    
    





