infor = {
    'name' : 'hello the fucking world ',
    'the year' : '2003',
    'description' : 'the fucking world',

}

print(infor)



infor['rating'] = '9.6'
print(infor)
key1 = input("New rating: ")
infor['rating'] = key1
print(infor)
key2 = input("You wanna delete : ")
del infor[key2]
print(infor)

# print('name' in infor)
if 'rating' in infor:
    print("Rating : exist")
else:
    print("Rating: Not found")

if 'name' in infor:
    print("Name : exist")
else:
    print("Name : Not found")