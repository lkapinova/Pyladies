from ai import tah_pocitace
from piskvorky import tah_hrace, vyhodnot, piskvorky1d
from util import tah
import pytest


# def test_tah():
#     assert tah(10*'-', 7, 'x') == '-------x--'
#     assert tah(10*'-', 0, 'x') == 'x---------'
#     assert tah(10*'-', 9, 'x') == '---------x'



# def test_tah_pocitace_strategie():
#     assert tah_pocitace('------o-o-', 'o', 'x') == '------ooo-'
#     assert tah_pocitace('----x-oox-', 'o', 'x') == '----xooox-'
#     assert tah_pocitace('-----xoo-x', 'o', 'x') == '-----xooox'
#     assert tah_pocitace('-x-x------', 'o', 'x') == '-xox------'
#     assert tah_pocitace('------xx--', 'o', 'x') == '-----oxx--'
#     assert tah_pocitace('-----oxx--', 'o', 'x') == '-----oxxo-'
#     assert tah_pocitace('--x-------', 'o', 'x') == '-ox-------'

#     assert tah_pocitace('------x-x-', 'x', 'o') == '------xxx-'
#     assert tah_pocitace('----o-xxo-', 'x', 'o') == '----oxxxo-'
#     assert tah_pocitace('-----oxx-o', 'x', 'o') == '-----oxxxo'
#     assert tah_pocitace('-o-o------', 'x', 'o') == '-oxo------'
#     assert tah_pocitace('------oo--', 'x', 'o') == '-----xoo--'
#     assert tah_pocitace('-----xoo--', 'x', 'o') == '-----xoox-'
#     assert tah_pocitace('--o-------', 'x', 'o') == '-xo-------'


# def test_tah_pocitace_random():
#     assert tah_pocitace('oxxoxo-xoxo', 'x', 'o') == 'oxxoxoxxoxo'


# def test_tah_pocitace_delka_pole():
#     assert tah_pocitace('-----oxxoxo-o--xoxo-----', 'x',
#                         'o') == '-----oxxoxoxo--xoxo-----'
#     assert tah_pocitace('xo-o--xo', 'x', 'o') == 'xoxo--xo'


def test_tah_pocitace_prazdne_pole():
    with pytest.raises(ValueError):
        tah_pocitace('', 'o', 'x')


def test_tah_pocitace_plne_pole():
    with pytest.raises(ValueError):
        tah_pocitace('xxooxxooxxooxx', 'o', 'x')
    

# def test_vyhodnot():
#     assert vyhodnot("oxxxo") == 'x'
#     assert vyhodnot("oxxoooxo") == 'o'
#     assert vyhodnot("oxxoxo") == '!'
#     assert vyhodnot("ox-oxo") == '-'


