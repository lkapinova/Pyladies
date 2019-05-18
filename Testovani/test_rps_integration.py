import rps
import subprocess


def input_faker(ret):
    def input_faked(prompt):
        print(prompt)
        return ret
    return input_faked

# MONKEYPATCH
# def test_game_asks_for_play(capsys, monkeypatch):
#     monkeypatch.setattr('builtins.input', input_faker('rock'))
#     rps.main()
#     captured = capsys.readouterr()
#     assert 'rock, paper or scissors?' in captured.out

# DEPENDENCY INJECTION
# def test_game_asks_for_play(capsys):
#     rps.main(input_faker('rock'))
#     captured = capsys.readouterr()
#     assert 'rock, paper or scissors?' in captured.out


def test_game_human_plays_rock(capsys):
    rps.main(input_faker('rock'))
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert 'rock, paper or scissors?' in lines[0]
    assert lines[1] in ('rock', 'paper', 'scissors')
    if lines[1] == 'rock':
        assert lines[2] == 'tie'