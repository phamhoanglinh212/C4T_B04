book = {
        'name' : 'I like my fucking world',
        'year' : '2003',
        'person' : ['MissFk', 'Hmm', 'Hmm1', 'Hmm2']
        # 'country' : ['Vietnam']
    }


# book.append(
#     {
#     'country' : 'Vietnam'    
#     }
    
# )
# print(book)

# book['person'].append('America')
# print(book)

# for key in book:
#     print(key, '-', book[key])

# for k,v in book.items():
    # print(k, '-', v)

book['person'] = ['MissMoney', 'Hmm', 'Hmm1', 'Hmm2']
# print(book)
book['person'].append('MrsMoney')
# print(book)
book['person'].remove('MissMoney')
# print(book)
# print(book['person'][0])
# for i in book['person']:
#     print(i)

for k,v in book.items():
    print(k,v)


