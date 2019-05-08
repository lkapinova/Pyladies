from dp_02 import tah, tah_hrace
import pytest

def test_tah_hrace():
    tah_hrace(10*'-', 'x', '7') == '-------x--'
    tah_hrace(10*'-', 'o', '0') == 'o---------'
    tah_hrace(10*'-', 'j', '9') == '---------j'
    tah_hrace(10*'-', 'x', '-3') == '----------'
    tah_hrace(10*'-', 'x', '12') == '----------'
    tah_hrace('---------j', 'x', '9') == '---------j'

def test_tah_hrace_TypeError():    
    with pytest.raises(TypeError):
        tah_hrace(10*'-', 'j', 'x')

