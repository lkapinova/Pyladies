from ai import tah_pocitace
from piskvorky import tah_hrace, vyhodnot, piskvorky1d
from util import tah

def test_tah():
    assert tah(10*'-',7,'x') == '-------x--'
    assert tah(10*'-',0,'x') == 'x---------'
    assert tah(10*'-',9,'x') == '---------x'


def test_tah_mimo_pole():
    try:
        assert tah(10*'-',10,'x')
    except ValueError:
        assert True

