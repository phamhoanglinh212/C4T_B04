while True:
    text = input("Enter your password : ")
    if text.isalpha():
        print("Try again!")
    else:
        print("OK")
        break