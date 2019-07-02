while True:
    diction = {
        'Supercalifragilisticexpialidocious' : 'Extraordinarily good',
        'Circumspect' : 'Comtemplate sthg before doing it',
        'Basorexia' : 'A strong desire of kissing',
        'Abditory' : 'A place you can disappear, a hiding place',
        'Clinomania' : 'A excesive desire to stay in bed',
        'Agoraphobia' : 'A fear of being in public places where are many other ppl' ,
        'Athazagoraphobia' : 'A fear of being forgotten or ignored',
        'Adultery' : 'Sex between a married person and sb who is not their husband or wife',
    }
    choose = input("Your word: ").upper()
    if choose == 'supercalifragilisticexpialidocious'.upper():
        print(diction['Supercalifragilisticexpialidocious'])
    elif choose == 'circumspect'.upper():
        print(diction['Circumspect'])
    elif choose == 'basorexia'.upper():
        print(diction['Basorexia'])
    elif choose == 'abditory'.upper():
        print(diction['Abditory'])
    elif choose == 'clinomania'.upper():
        print(diction['Clinomania'])
    elif choose == 'agoraphobia'.upper():
        print(diction['Agoraphobia'])
    elif choose == 'athazagoraphobia'.upper():
        print(diction['Athazagoraphobia'])
    elif choose == 'adultery'.upper():
        print(diction['Adultery'])
    else:
        print("Not found in our dictionary. Please try other words")

    conti = input("You wanna continue? (Y/N)  ").upper()
    if conti == 'Y':
        print("Loading...")
    elif conti == 'N':
        print("Thank you")
        break
    else:
        print("ERROR")
        break