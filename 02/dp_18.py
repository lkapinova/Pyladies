print('Odpovídej "ano" nebo "ne".')

stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')

if stastna:
    if bohata:
        # Je bohatá a zároveň štǎstná, ta se má.
        print('Gratuluji!')
    else:
        # Tady musí být jen šťastná.
        print('Zkus se víc usmívat.')
    
if bohata and not stastna:
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá.
    print('Zkus míň utrácet.')

if not stastna and not bohata:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')
