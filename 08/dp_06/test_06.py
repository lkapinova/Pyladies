import pytest
from dp_06 import pohyb

def test_pohyb():
    pohyb([(0, 0), (1, 0)], 'v')
    # assert len(seznam_souradnic) == 3
    assert nove_souradnice == (2, 0)

def test_pohyb():
    pohyb([(0, 0), (1, 0), (2, 0)], 'z')
    # assert len(seznam_souradnic) == 4
    assert nove_souradnice == (1, 0)

def test_pohyb():
    pohyb([(0, 0), (1, 1), (2, 1), (2, 2)], 's')
    # assert len(seznam_souradnic) == 5
    assert nove_souradnice == (2, 1)

def test_pohyb():
    pohyb([(1, 1)], 'j')
    # assert len(seznam_souradnic) == 2
    assert nove_souradnice == (1, 2)
