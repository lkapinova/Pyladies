from ai import tah_pocitace
from piskvorky import tah_hrace, vyhodnot, piskvorky1d
from util import tah
import pytest


def test_tah():
    assert tah(10*'-', 7, 'x') == '-------x--'
    assert tah(10*'-', 0, 'x') == 'x---------'
    assert tah(10*'-', 9, 'x') == '---------x'


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


def test_vyhodnot():
    assert vyhodnot("oxxxo") == 'x'
    assert vyhodnot("oxxoooxo") == 'o'
    assert vyhodnot("oxxoxo") == '!'
    assert vyhodnot("ox-oxo") == '-'
