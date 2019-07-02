infor = [
    {
        'name' : 'Huy',
        'role' : 'waiter',
        'hours' : 12,
        'salary' : 0.8,
    },
    {
        'name' : 'Tung',
        'role' : 'cook',
        'hours' : 24,
        'salary' : 1.5,
    },
    {
        'name' : 'M.Duc',
        'role' : 'manager',
        'hours' : 20,
        'salary' : 2,
    }
]

for u in infor:
    print(u)

salary1 = (infor[1]['salary'])
hour1 = (infor[1]['hours'])
total1 = salary1 * hour1
print(total1)

salary2 = (infor[2]['salary'])
hour2 = (infor[2]['hours'])
total2 = salary2 * hour2
print(total2)

salary0 = (infor[0]['salary'])
hour0 = (infor[0]['hours'])
total0 = salary0 * hour0
print(total0)

totallast = total1 + total2 + total0
print(totallast)