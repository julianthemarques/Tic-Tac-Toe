# Project tic tac toe

board = ['_','_','_',
         '_','_','_',
         '_','_','_']


def has_winner():
    if board[0] == board[1] and board[0] == board[2] and board[0] != '_':
        return True
    elif board[0] == board[3] and board[0] == board[6] and board[0] != '_':
        return True
    elif board[0] == board[4] and board[0] == board[8] and board[0] != '_':
        return True
    elif board[6] == board[4] and board[6] == board[2] and board[6] != '_':
        return True
    elif board[6] == board[7] and board[6] == board[8] and board[8] != '_':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board [1] != '_':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != '_':
        return True
    elif board[3] == board[4] and board[3] == board[5] and board[3] != '_':
        return True

def draw():
    if board[0] != '_' and board[1] != '_' and board[2] != '_' and board[3] != '_' and board[4] != '_' and board[5] != '_' and board[6] != '_' and board[7] != '_' and board[8] != '_':
        print('draw!')
        return True
    

def displaytheboard():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')


def make_play(current_player):
    position = int(input(f'Player {current_player} [1/9]: '))
    position = position - 1
    while board[position] != '_':
        print('invalid position, make a new play: ')
        position = int(input(f'Player {current_player} [1/9]: '))
        position = position - 1
        
    board[position] = current_player

current_player = 'X'

print("Welcome to the Tic Tac Toe game,let's start to play...")

while True:
    #actual play
    displaytheboard()
    make_play(current_player)
    if has_winner():
        displaytheboard()
        print(f'Player {current_player} has won!')
        print('End of game!')
        break
    current_player = 'O' if current_player == 'X' else 'X'
    if draw():
        print('End of game!')
        break
    