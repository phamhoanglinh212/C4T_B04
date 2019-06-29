highscores = [45, 50, 60, 13, 98]
highscores.sort(reverse=True)

for i, items in enumerate(highscores):
    print(i + 1 , ". ", items)
while True:
    new = int(input("Enter your new scores : "))
    highscores.append(new)
    highscores.sort(reverse=True)
    for i, items in enumerate(highscores):
        if i < 5:
            print(i + 1 , ". ", items)
    
