try:
    x = int(input('X = '))
    y = int(input('Y = '))
    if x == 0:
        print('X is zero ... ')
        raise Exception()
    z = x/y
    print(z)
except:
    if x == 0:
        print('X is zero ... in the exception')
    else:
        print("y is zero ...")

print('oh my ....')

print('-----------------------------------------')

