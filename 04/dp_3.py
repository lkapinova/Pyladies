def mala_nasobilka(n):
    for i in range(n+1):
        for j in range(n+1):
            print(i*j,end=' ')
        print()

mala_nasobilka(5)