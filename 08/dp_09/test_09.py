import pytest
from dp_09 import pohyb


def test_v_pohyb():
    souradnice = [(1, 1)]
    pohyb(souradnice, 'j')
    assert len(souradnice) == 1
    assert souradnice[-1] == (1, 2)


def test_z_pohyb():
    souradnice = [(3, 0), (3, 1), (3, 2)]
    pohyb(souradnice, 'z')
    assert len(souradnice) == 3
    assert souradnice[-1] == (2, 2)


def test_s_pohyb():
    souradnice = [(3, 0), (3, 1), (4, 2), (3, 3)]
    pohyb(souradnice, 's')
    assert len(souradnice) == 4
    assert souradnice[-1] == (3, 2)


def test_j_pohyb():
    souradnice = [(1, 1)]
    pohyb(souradnice, 'j')
    assert len(souradnice) == 1
    assert souradnice[-1] == (1, 2)


def test_out_of_map_pohyb():
    souradnice = [(7, 0), (8, 0), (9, 0)]
    with pytest.raises(ValueError):
        pohyb(souradnice, 'v')


def test_same_coords_pohyb():
    souradnice = [(7, 0), (8, 0), (9, 0)]
    with pytest.raises(ValueError):
        pohyb(souradnice, 'z')
