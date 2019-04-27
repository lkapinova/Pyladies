import pytest
from dp_06 import pohyb


def test_v_pohyb():
    souradnice = [(1, 1)]
    pohyb(souradnice, 'j')
    assert len(souradnice) == 2
    assert souradnice[-1] == (1, 2)


def test_z_pohyb():
    souradnice = [(0, 0), (1, 0), (2, 0)]
    pohyb(souradnice, 'z')
    assert len(souradnice) == 4
    assert souradnice[-1] == (1, 0)


def test_s_pohyb():
    souradnice = [(0, 0), (1, 1), (2, 1), (2, 2)]
    pohyb(souradnice, 's')
    assert len(souradnice) == 5
    assert souradnice[-1] == (2, 1)


def test_j_pohyb():
    souradnice = [(1, 1)]
    pohyb(souradnice, 'j')
    assert len(souradnice) == 2
    assert souradnice[-1] == (1, 2)
