from random import randrange

def kamen_nuzky_papir():
    cislo = randrange(3)

    if cislo == 0:
        tah_pocitace = 'kámen'
    elif cislo == 1:
        tah_pocitace = 'nůžky'
    else:
        tah_pocitace = 'papír'

    tah_cloveka = input('kámen, nůžky, nebo papír? ')

    if tah_cloveka == 'kámen':
        if tah_pocitace == 'kámen':
            print('Plichta.')
        elif tah_pocitace == 'nůžky':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'papír':
            print('Počítač vyhrál.')
    elif tah_cloveka == 'nůžky':
        if tah_pocitace == 'kámen':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'nůžky':
            print('Plichta.')
        elif tah_pocitace == 'papír':
            print('Vyhrála jsi!')
    elif tah_cloveka == 'papír':
        if tah_pocitace == 'kámen':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'nůžky':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'papír':
            print('Plichta.')
    else:
        print('Nerozumím.')

    print("Počítač zvolil "+ tah_pocitace)

while True:
    nova_hra = input("Chceš si zahrát kámen, nůžky, papír? Odpovídej ano/ne: \n")
    if nova_hra == "ano":
        kamen_nuzky_papir()
    elif nova_hra == "ne":
        print("Díky za hru.")
        break
    else:
        print('Nerozumím.')
    