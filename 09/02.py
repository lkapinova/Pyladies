# Cena jizdneho
# 1. Deti do 10 let vcetne jezdi zadarmo
# 2. Mladez do 18 vcetne let jezdi za polovinu
# 3. Seniori od 65 let vcetne jezdi za tretinu
# 4. Ostatni jezdi za plnou cenu
# 5. Zaporny vek musi skoncit vyjimkou ValueError

# import pytest

def spocitej_slevu_jizdneho(zakladni_cena, vek):
    if vek < 0:
        raise ValueError
    elif vek <=10:
        return 0
    elif vek <=18:
        return zakladni_cena / 2
    elif vek < 65:
        return zakladni_cena
    else:
        return zakladni_cena / 3

def test_deti_jezdi_zdarma():
    assert spocitej_slevu_jizdneho(10,5) == 0

def test_cena_senior():
    assert spocitej_slevu_jizdneho(30,65) == 10

def test_cena_pro_mladistve():
    assert spocitej_slevu_jizdneho(20,17) == 10
    assert spocitej_slevu_jizdneho(20,18) == 10
    assert spocitej_slevu_jizdneho(20,11) == 10

def test_cena_pro_dospele():
    assert spocitej_slevu_jizdneho(50,35) == 50
    assert spocitej_slevu_jizdneho(50,19) == 50
    assert spocitej_slevu_jizdneho(50,64) == 50

def test_zaporny_vek_vyjimka():
    try:
        spocitej_slevu_jizdneho(10,-4)
        # assert False
    except ValueError:
        assert True     # nebo 'pass' - to nic nedělá
    else:
        assert False

