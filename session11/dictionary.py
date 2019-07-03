computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}

computer['TOSHIBA'] = 10 
print(computer)

print('Tổng: ',sum(computer.values()))


# sum1 = sum("computer".value())
# print(sum1)


# sum1 = computer['HP'] + computer['DELL'] + computer['MACBOOK'] + computer['ASUS']
# print('Tổng: ', sum1)










# for k,v in computer.items():
#     print(k, ':', v)
# print('-'*20)
# choose = input("May tính muốn kiểm tra số lượng: ").upper()
# print(computer[choose])

# print('-'*20)
# choose1 = input("Your type of computer: ")
# choose2 = int(input("Your number: "))
# computer[choose1] = choose2
# for k,v in computer.items():
#     print(k, ':', v)

# print('-'*20)
# add = computer['HP'] + 20
# print(add)

# add1 = computer['MACBOOK'] - 2
# print(add1)

# print('-'*20)
# print(computer['MACBOOK'])