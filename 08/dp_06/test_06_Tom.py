import pytest
from dp_06 import pohyb

def do_test_souradnice(souradnice, smer, delka, posledni_souradnice):
    pohyb(souradnice, smer)
    assert len(souradnice) == delka
    assert souradnice[-1] == posledni_souradnice

def test_v_pohyb():
    do_test_souradnice([(0, 0), (1, 0)], 'v', 3, (2,0))

def test_z_pohyb():
    do_test_souradnice([(0, 0), (1, 0), (2, 0)], 'z', 4, (1,0))

def test_s_pohyb():
    do_test_souradnice([(0, 0), (1, 1), (2, 1), (2, 2)], 's', 5, (2,1))


def test_j_pohyb():
    do_test_souradnice([(1, 1)], 'j', 2, (1,2))
    