numbers = [2, 12, 15, 6, 25, 11, 24, 10]
numChoose = int(input("The number you choose : "))
if numChoose in numbers:
    for c,d in enumerate(numbers, 1):
        if d == numChoose:
            print("Found",numChoose,"at position",c)


else:
    print("Not found in our list ")
