game = [
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
for i in range(len(game)):
    for e, k in enumerate(game[i].values()):
        print(e,':',k)