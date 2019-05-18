import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock':
        if computer == 'scissors':
            return 'human'
        else:
            return 'computer'
    elif human == 'paper':
        if computer == 'rock':
            return 'human'
        else:
            return 'computer'
    else:
        if computer == 'paper':
            return 'human'
        else:
            return 'computer'

def main(load=input):
    human = None
    while not is_valid_play(human):
        human = load('rock, paper or scissors? ')

    computer = random_play()
    print(computer)
    print(determine_game_result(human, computer))

if __name__ == '__main__':
    main()
    
