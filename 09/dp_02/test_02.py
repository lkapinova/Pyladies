from dp_02 import tah, tah_hrace
import pytest

def test_tah_hrace():
    tah(10*'-', 7, 'x') == '-------x--'
    tah(10*'-', 0, 'o') == 'o---------'
    tah(10*'-', 9, 'j') == '---------j'
    tah(10*'-', -3, 'x') == '----------'
    tah(10*'-', 12, 'x') == '----------'
    tah(10*'-', 12, 'x') == '----------'
    
    with pytest.raises(TypeError):
        tah(10*' ', 'j', 'x')

