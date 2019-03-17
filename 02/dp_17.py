from random import randrange

number = randrange(3)
if number == 0:
    PC = 'kámen'
elif number == 1:
    PC = 'nůžky'
else:
    PC = 'papír'

Player = input('kámen, nůžky, nebo papír? ')

if PC == Player:
    print('Plichta.')
elif (PC == 'kámen' and Player == 'nůžky') or (PC == 'nůžky' and Player == 'papír') or (PC == 'papír' and Player == 'kámen'):
    print('Počítač vyhrál.')
elif (Player == 'kámen' and PC == 'nůžky') or (Player == 'nůžky' and PC == 'papír') or (Player == 'papír' and PC == 'kámen'):
    print('Vyhrála jsi!')
else:
    print('Nerozumím.')

print("Počítač zvolil "+ PC)