def secti(a, b):
    try:    
        a = int(a)
        b = int(b)
    except ValueError:
        print("neplatny vstup")
        return None

    return a + b

def test_secti():
    assert secti(2, 3) == 5
    assert secti("1", "0") == 1
    assert secti("a", "0") == None