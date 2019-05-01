from ai import tah_pocitace
from piskvorky import tah_hrace, vyhodnot, piskvorky1d
from util import tah
import pytest


def test_tah():
    assert tah(10*'-', 7, 'x') == '-------x--'
    assert tah(10*'-', 0, 'x') == 'x---------'
    assert tah(10*'-', 9, 'x') == '---------x'


def test_tah_mimo_pole():
    try:
        assert tah(10*'-', 10, 'x')
    except ValueError:
        assert True


def test_tah_zaporna_pozice():
    try:
        assert tah(10*'-', -2, 'x')
    except ValueError:
        assert True


def test_tah_plne_pole():
    try:
        assert tah('xoxoxoxo', 3, 'x')
    except ValueError:
        assert True


def test_tah_pocitace_strategie():
    assert tah_pocitace('------o-o-') == '------ooo-'
    assert tah_pocitace('----x-oox-') == '----xooox-'
    assert tah_pocitace('-----xoo-x') == '-----xooox'
    assert tah_pocitace('-x-x------') == '-xox------'
    assert tah_pocitace('------xx--') == '-----oxx--'
    assert tah_pocitace('-----oxx--') == '-----oxxo-'
    assert tah_pocitace('--x-------') == '-ox-------'


def test_tah_pocitace_random():
    assert tah_pocitace('oxxoxo-xoxo') == 'oxxoxooxoxo'

def test_tah_pocitace_plne_pole():
    try:
        assert tah_pocitace('xoxoxoxo')
    except ValueError:
        assert True

def test_vyhodnot():
    assert vyhodnot("oxxxo") == 'x'
    assert vyhodnot("oxxoooxo") == 'o'
    assert vyhodnot("oxxoxo") == '!'
    assert vyhodnot("ox-oxo") == '-'


def test_vyhodnot_nesmysl():
    try:
        assert vyhodnot('kkkrkrkkr')
    except ValueError:
        assert True
