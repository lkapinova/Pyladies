def ramecek(sirka,vyska):
    for i in range (vyska):
        if i == 0 or i == vyska-1:
            for j in range(sirka):
                print('x', end=' ')
            print()
        else:
            for l in range(sirka):
                if l == 0:
                    print('x', end=" ")
                elif l == sirka - 1:
                    print('x')
                else:
                    print(' ', end=' ')

ramecek(5,10)
ramecek(10,15)