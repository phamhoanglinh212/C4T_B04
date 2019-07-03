import random
while True:
    things = ['money1', 'money2', 'money3', 'money4', 'money5']
    word = random.choice(things)
    split = list(word)
    random.shuffle(split)
    print("Shuffle : ", *split, sep='  ')
    word2 = input("Your answer : ")
    emerge = ''.join(split)
    if word2 == emerge:
        print("Correct")
        break
    elif word2 != emerge:
        print("Try again")