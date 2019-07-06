from random import *
while True:
    x = randint(0, 100)
    y = randint(0, 100)
    z = randint(-1, 1)
    c = x + y
    d = x + y + z
    print(x)
    print(y)
    print(c)
    print(x, "+", y, "=", d )
    result = input("YES or NO : ").upper()
    
    if c != d:
        if result == "NO":
            print("Correct")
        elif result == "YES":
            print("Game over")
            break
    else:
        if result  == "YES":
            print("Correct")
        elif result == "NO":
            print("Game over")
            break   
                