color = ['red', 'blue', 'green', 'pink']
print(*color, sep=', ')
add = input("Your new color : ")
color.append(add)
print("New list: ",end="") 
print(*color, sep=', ')



