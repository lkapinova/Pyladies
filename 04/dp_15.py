def ramecek(rozmer):
    for i in range (rozmer):
        if i == 0:
            print(rozmer*'x ')
        if i == rozmer-1:
            print(rozmer*'x ')
        else:
            print('x' + (2*rozmer-3)*' ' + 'x')

ramecek(15)