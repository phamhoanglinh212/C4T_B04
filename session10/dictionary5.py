
game = [
    {
        'name' : 'Name of the film?',
        'result' : 'The fucking world',
        'choice' : ['A. Shove your mouth up yout butt', 'B. Adultery', 'C. The fuking world']
    },
    {
        'name' : 'Year? ',
        'result' : '2003',
        'choice' : ['A. 2009', 'B. 2003', 'C. 1991']
    }
]

correct = 0
incorrect = 0

print(game[0]['name'])
for i in game[0]['choice']:
    print(i)
choice = input("Your answer: ").upper()
if choice == 'A'.upper():
    incorrect += 1
    print('Incorrect')
elif choice == 'B'.upper():
    incorrect += 1
    print('Incorrect')
elif choice == 'C'.upper():
    correct +=1
    print('Correct')
else:
    incorrect +=1
    print('Error')

print('-'*20)


print(game[1]['name'])
for i in game[1]['choice']:
    print(i)
choice = input("Your answer: ").upper()
if choice == 'A'.upper():
    incorrect +=1
    print('Incorrect')
elif choice == 'C'.upper():
    incorrect +=1
    print('Incorrect')
elif choice == 'B'.upper():
    correct +=1
    print('Correct')
else:
    incorrect +=1
    print('Error')

print("Số câu trả lời đúng: ", correct)
print("Số câu trả lời sai: ", incorrect)

percent = correct / (correct+incorrect) * 100
print("Phần trăm trả lời đúng: ", percent, '%')







# print(game['name'])
# for i in game['choice']:
#     print(i)
# choice = input("Your answer: ")
# if choice != game['result']:
#     print('Try again')
# elif choice == game['result']:
#     print('Correct')





