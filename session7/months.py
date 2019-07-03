n = int(input("Enter your number : "))
if 0<n<9:
    for i in range(0, 9): 
        if n % 2 != 0: 
            print("This month has 31 days")
            break
        elif n == 2:
            print("This month has 28 days")
            break
        elif n == 8:
            print("This month has 31 days")
            break
        else:
            print("This month has 30 days")
            break
elif 8<n<13:
    for i in range(8, 13): 
        if n % 2 != 0: 
            print("This month has 30 days")
            break
        else:
            print("This month has 31 days")
            break


        