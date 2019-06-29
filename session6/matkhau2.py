while True:
    text = input("Enter your password : ")
    length = len(text)
    if length < 8:
        print("Try again")
    elif text.isalpha():
        print("Try again")
    else:
        print("Ok")
        break
