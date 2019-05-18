import random

human = input('rock, paper or scissors? ')

while human not in ['rock', 'paper', 'scissors']:
    human = input('rock, paper or scissors? ')

computer = random.choice(['rock', 'paper', 'scissors'])

print(computer)

if human == computer:
    print('it\'s a tie!')
elif human == 'rock':
    if computer == 'scissors':
        print('You win!')
    else:
        print('Computer win!')
elif human == 'paper':
    if computer == 'rock':
        print('You win!')
    else:
        print('Computer win!')
else:
    if computer == 'paper':
        print('You win!')
    else:
        print('Computer win!')
