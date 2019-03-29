def ramecek(sirka,vyska):
    for i in range (vyska):
        if i == 0:
            print(sirka*'x ')
        if i == vyska-1:
            print(sirka*'x ')
        else:
            print('x' + (2*sirka-3)*' ' + 'x')

ramecek(5,10)
ramecek(10,15)