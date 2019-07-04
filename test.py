
game = [
    {
        'name' : 'Name of the film?',
        'result' : 'The fucking world',
        'choice' : ['A. Shove your mouth up yout butt', 'B. Adultery', 'C. The fuking world'],
        'choiceCorrect':'C',
    },
    {
        'name' : 'Year? ',
        'result' : '2003',
        'choice' : ['A. 2009', 'B. 2003', 'C. 1991'],
        'choiceCorrect':'A',
    }
]

correct = 0
incorrect = 0
# print(game[0]['choiceCorrect'])
for i in range(len(game)):
    print(game[i]['name'])
    for j in game[i]['choice']:
        print(j)
    choice = input("Your answer: ").upper()
    if choice == str(game[i]['choiceCorrect']):
        correct +=1
        print('Correct')
    else:
        incorrect += 1
        print('Incorrect')
        


print("Số câu trả lời đúng: ", correct)
print("Số câu trả lời sai: ", incorrect)

percent = correct / (correct+incorrect) * 100
print("Phần trăm trả lời đúng: ", percent, '%')












