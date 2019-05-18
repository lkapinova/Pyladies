import subprocess
import sys

def run_rps(input):
    return subprocess.run(
        [sys.executable, 'rps.py'],
        stdout=subprocess.PIPE,
        encoding='utf-8',
        input=input,
        check=True
    )

def test_wrong_play_results_in_repeated_question():
    cp = run_rps('blah\nrock\n')  
    print(cp.stdout) 
    assert cp.stdout.count('rock, paper or scissors?') == 2