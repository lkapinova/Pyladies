import pytest

def vyhodnot(piskvorky):
    "Funkce vyhodnotí 1D piškvorky. Pro vítězství jsou nutné tři znaky v řadě."

    if "xxx" in piskvorky:
        vysledek = 'x'
    elif "ooo" in piskvorky:
        vysledek = 'o'
    elif "-" not in piskvorky:
        raise ValueError
    else:
        vysledek = '-'
    return vysledek


def test_vyhodnot():
    testovaci_vstup0 = '-----------------'
    testovaci_vstup1 = '-----ooo------------'
    testovaci_vstup2 = '--------xxx---------'
    testovaci_vstup3 = 'oxoxoxoxoxoxoxo'

    assert vyhodnot(testovaci_vstup0) == '-'
    assert vyhodnot(testovaci_vstup1) == 'o'
    assert vyhodnot(testovaci_vstup2) == 'x'
    # assert vyhodnot(testovaci_vstup3) == '!'
    
    with pytest.raises(ValueError):
        vyhodnot(testovaci_vstup3)
        raise AssertionError('Test selhal')