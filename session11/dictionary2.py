dict_list = [
    {
        'HP':20,
        'DELL':50,
        'MACBOOK':12,
        'ASUS':30,
    },
    {
        'HP': 600,
        'DELL': 650,
        'MACBOOK': 12000,
        'ASUS': 400,
        'ACER': 350,
        'TOSHIBA': 600,
        'FUJITSU': 900,
        'ALIENWARE': 1000,
    }
]
for k,v in dict_list[0].items():
    print(k,':',v)
print('-'*20)
dict_list[0]['TOSHIBA'] = 10 
dict_list[0]['DELL'] = dict_list[0]['DELL']+ 10
dict_list[0]['MACBOOK'] = dict_list[0]['MACBOOK'] - 2
dict_list[0]['FUJITSU '] = 15
dict_list[0]['ALIENWARE'] = 5
for k,v in dict_list[0].items():
    print(k,':',v)
print('-'*20)
for k,v in dict_list[1].items():
    print(k,':',v,'USD')
print('-'*20)
ten = dict_list[0].keys()
soluong= dict_list[0].values()
gia = dict_list[1].values()
# sum = 0
for y,u,e in zip(ten,soluong, gia):
    tong = u*e
    print(y,tong)

# for tong in range(6):
#     sum = sum + tong
#     print(sum)
