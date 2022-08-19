message = 'String ....'

print(message)
result = len(message)
print(message, ' : ' , result)

print('-------------------------------------')
result = 'ing' in message
print(result)

mess = '0891145553'
result = mess.isdigit()
print(result)
print(type(result))

print('-------------------------------------')
print(message.upper())
print(mess.upper())
print(message.lower())
print(mess.lower())

print('-------------------------------------')
message = 'Just Python'
result = message.replace('Python', 'PPPPPYYYYY')
print(message, result)

print('-------------------------------------')
message = 'rabbit, squarrel, bear'
print(message)
animals = message.split(', ')
new_message = '++++'.join(animals)
print('message : ', message)
print('new_message : ', new_message)
print('animals : ', animals)


