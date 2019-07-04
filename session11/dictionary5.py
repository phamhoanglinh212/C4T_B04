from random import*
skill = [
    {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3,
    },
    {
        'Name': 'Quick attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5,
    },
    {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2,
    },
]
# print(skill[0]['Minimum level'])
random1 = randint(0,1)
level = int(input("Your current level: "))
choose = int(input("Your skill you want: "))
for i in range(len(skill)):
    if skill[choose] == skill[i]:
        if level >= skill[i]['Minimum level']:
            print('Level tối thiểu: ', skill[i]['Minimum level'])
            if random1 < skill[i]['Hit rate']:
                print(skill[i]['Damage'])
            elif random1 > skill[i]['Hit rate']:
                print('Không trúng mục tiêu')
        elif level < skill[i]['Minimum level']:
            print('Không đủ điều kiện')
            