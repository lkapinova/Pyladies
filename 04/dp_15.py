def ramecek(rozmer):
    "nakreslí rámeček složený z x"
    for i in range (rozmer):
        if i == 0 or i == rozmer-1:
            for j in range(rozmer):
                print('x', end=' ')
            print()
        else:
            for l in range(rozmer):
                if l == 0:
                    print('x', end=" ")
                elif l == rozmer - 1:
                    print('x')
                else:
                    print(' ', end=' ')

ramecek(27)