import pytest
from obrazek import nakresli_obesence
from obesenec import slovo_to_string, dopln_pismeno, vyhodnoceni, hrat_obesence


def test_slovo_to_string():
    assert slovo_to_string("kometa") == "-"*6
    assert slovo_to_string("popocatepetl") == "-"*12

def test_slovo_to_string_int():
    try:
        assert slovo_to_string(7)
    except TypeError:
        return True

def test_slovo_to_string_prazdny_string():
    assert slovo_to_string("") == ""

def test_dopln_pismeno():
    assert dopln_pismeno("-----", "a", 2) == "--a--"
    assert dopln_pismeno("-----", "a", 0) == "a----"
    assert dopln_pismeno("-----", "a", 4) == "----a"

def test_dopln_pismeno_invalid_input():
    try:
        assert dopln_pismeno("-----", 7, 4)
    except TypeError:
        return True
    try:
        assert dopln_pismeno("-----", "a", "b")
    except TypeError:
        return True

def test_dopln_pismeno_prazdny_retezec():
    try:
        assert dopln_pismeno("", "a", 5)
    except AssertionError:
        return True

