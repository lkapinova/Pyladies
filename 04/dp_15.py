def ramecek(rozmer):
    for i in range (rozmer):
        if i == 0:
            for j in range(rozmer):
                print('x', end=' ')
            print()
        if i == rozmer-1:
            for k in range(rozmer):
                print('x', end=' ')
            print()
        else:
            print('x' + (2*rozmer-3)*' ' + 'x')

ramecek(15)