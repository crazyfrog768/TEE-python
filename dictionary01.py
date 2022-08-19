book = {'name':'c++', 'price': 309, 'page':414}

print(book)
print(book['name'])
print(book['price'])
print(book['page'])

print('-------------------------------------')
book['price'] = 500
print(book)

book['place'] = 'chula'
print(book)

book.pop('price')
print(book)
