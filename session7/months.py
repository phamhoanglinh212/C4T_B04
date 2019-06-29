n = int(input("Enter your number : "))
for i in range(0, 13): 
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
    


        