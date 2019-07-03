computer = {
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}
for k,v in computer.items():
    print(k,':',v)

# computer['TOSHIBA'] = 10 
# computer['HP'] = computer['HP']+ 20
# computer['MACBOOK'] = computer['MACBOOK'] - 2
# print(computer)
choose = input("Your computer: ").upper()
choose1 = int(input("Xuất: "))
computer[choose] = computer[choose] - choose1
print('-'*20)
print('Bảng mới: ')
for k,v in computer.items():
    print(k, ':',v)





# choose = input("Your computer: ").upper()
# # print('Price: ', computer[choose], 'USD'
# choose1 = int(input("Số lượng: "))
# total = computer[choose] * choose1
# print('Tổng giá trị đơn hàng: ', total)