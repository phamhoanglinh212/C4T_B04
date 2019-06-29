while True:
    import random
    things = ['money1', 'money2', 'money3', 'money4', 'money5']
    word = random.choice(things)
    split = list(word)
    random.shuffle(split)
    print("Shuffle : ", *split, sep='  ')
    word2 = input("Your answer : ")
    emerge = ''.join(split)
    if word2 == word:
        print("Correct")
        print("-"*20)
    else:
        print("Error")
        print("-"*20)
    conti = input("Next round ?(y/n): ").upper()
    if conti == "N":
        print("Thanks for playing")
        break
    elif conti == "Y":
        print("Loading...")
    else:
        print("Try again")
    





