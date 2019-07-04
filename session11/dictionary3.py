infor = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2,
}

for e,f in infor.items():
    print(e,':',f)
infor['Gold'] = infor['Gold'] + 50
for e,f in infor.items():
    print(e,':',f)
infor['Backpack'].append(['FlintStone', 'Backback'])
for e,f in infor.items():
    print(e,':',f)
infor['Pocket '] = ['MonsterDex', 'Flashlight']
for e,f in infor.items():
    print(e,':',f)