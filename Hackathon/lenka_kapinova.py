import random
# from util import tah


def tah_pocitace(herni_pole, pc_symbol, symbol_hrac):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if herni_pole == '':
        raise ValueError('Pole nemůže být prázdné')

    if '-' not in herni_pole:
        raise ValueError('Alespoň jedno políčko v herním poli musí být volné.')

    if (pc_symbol+"-"+pc_symbol) in herni_pole:
        policko = herni_pole.find(pc_symbol+"-"+pc_symbol)
        herni_pole = tah(herni_pole, (policko+1), pc_symbol)
    elif ("-"+2*pc_symbol) in herni_pole:
        policko = herni_pole.find("-"+2*pc_symbol)
        herni_pole = tah(herni_pole, policko, pc_symbol)
    elif (2*pc_symbol+"-") in herni_pole:
        policko = herni_pole.find(2*pc_symbol+"-")
        herni_pole = tah(herni_pole, (policko+2), pc_symbol)
    elif (symbol_hrac+"-"+symbol_hrac) in herni_pole:
        policko = herni_pole.find(symbol_hrac+"-"+symbol_hrac)
        herni_pole = tah(herni_pole, (policko+1), pc_symbol)
    elif ("-"+2*symbol_hrac) in herni_pole:
        policko = herni_pole.find("-"+2*symbol_hrac)
        herni_pole = tah(herni_pole, policko, pc_symbol)
    elif (2*symbol_hrac+"-") in herni_pole:
        policko = herni_pole.find(2*symbol_hrac+"-")
        herni_pole = tah(herni_pole, (policko+2), pc_symbol)
    elif ("-"+symbol_hrac+"-") in herni_pole:
        policko = herni_pole.find("-"+symbol_hrac+"-")
        herni_pole = tah(herni_pole, (policko), pc_symbol)
    else:
        delka_pole = len(herni_pole)
        while True:
            tah_pc = random.randrange(0, delka_pole)
            if herni_pole[tah_pc] == '-':
                herni_pole = tah(herni_pole, tah_pc, pc_symbol)
                break

    return herni_pole
