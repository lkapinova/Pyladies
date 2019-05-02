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
    assert tah_pocitace('------o-o-','o','x') == '------ooo-'
    assert tah_pocitace('----x-oox-','o','x') == '----xooox-'
    assert tah_pocitace('-----xoo-x','o','x') == '-----xooox'
    assert tah_pocitace('-x-x------','o','x') == '-xox------'
    assert tah_pocitace('------xx--','o','x') == '-----oxx--'
    assert tah_pocitace('-----oxx--','o','x') == '-----oxxo-'
    assert tah_pocitace('--x-------','o','x') == '-ox-------'

    assert tah_pocitace('------x-x-','x','o') == '------xxx-'
    assert tah_pocitace('----o-xxo-','x','o') == '----oxxxo-'
    assert tah_pocitace('-----oxx-o','x','o') == '-----oxxxo'
    assert tah_pocitace('-o-o------','x','o') == '-oxo------'
    assert tah_pocitace('------oo--','x','o') == '-----xoo--'
    assert tah_pocitace('-----xoo--','x','o') == '-----xoox-'
    assert tah_pocitace('--o-------','x','o') == '-xo-------'


def test_tah_pocitace_random():
    assert tah_pocitace('oxxoxo-xoxo','x','o') == 'oxxoxoxxoxo'

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
