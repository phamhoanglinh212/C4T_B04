list1 = {
    '1':'Show all songs',
    '2':'Show detail a song',
    '3':'Play a song',
    '4':'Search and download songs',
    '5':'Exit',
}
for k,v in list1.items():
    print(k,'.',v)
while True:
    choose = input("Pick one of a options: ")
    # print(list1[choose])
    if choose == '1':
        print("Song list is empty")
    elif choose == '2':
        print("Song list is empty")
    elif choose == '3':
        print("Song list is empty")
    elif choose == '5':
        break
    elif choose == '4':
        
