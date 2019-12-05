## print('Welcome to Tic Tac Toe!')
# Set up the board and display
from IPython.display import clear_output

board = ['.' for i in range(0, 9)]


def display_board(board):
    if len(board) == 9:
        print(board[:3])
        print(board[3:6])
        print(board[6:])
    else:
        print('Board Error')


display_board(board)

# Player1 or 2 to choose a marker
import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player1 choose a marker'
    else:
        return 'Player2 choose a marker'


# variable to get selected user form function call
playerselection = choose_first()


# input function to get the correct marker
def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input(playerselection + ' X or O: ').upper()
    if marker == 'X':
        return ("X", "O")
    else:
        return ("O", "X")


player_marker = player_input()

# global variale to start the game
game_on = True

# global variable to mark player1 turn. 0 is player 1 and 1 is player 2
player_turn = 0


# placemarker for particular position
def place_marker(board, marker, position):
    board[position] = marker


# to check which position has a space
def space_check(board, position):
    return board[position] == '.'


# asking the player to input position on the board
def player_choice(board):
    position = int(input('Please enter next position: '))

    while position not in (range(0, 9)) or not space_check(board, position):
        position = int(input('Please enter a free position: '))
    return position


# checking if board is full or not
def full_board_check(board):
    for i in range(0, 9):
        if space_check(board, i) == True:
            return False
    return True


# function for combinations of wins
def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))


# Function to tell us if we want to replay or not
def replay():
    playagain = ''

    while playagain.upper() != 'Y' and playagain.upper() != 'N':
        playagain = input('Enter "Y" or "N": ')
    if playagain.upper() == 'Y':
        return True
    elif playagain.upper() == 'N':
        return False


while game_on:

    marker = player_marker[player_turn]

    position = player_choice(board)

    place_marker(board, marker, position)
    clear_output()
    display_board(board)
    player_number = player_turn + 1

    if win_check(board, marker):
        display_board(board)
        print('Player ' + str(player_number) + ' is the winner')
        game_on = False

    elif full_board_check(board):
        display_board(board)
        print('This is a draw')

        if replay() == True:
            clear_output()
            board = ['.' for i in range(0, 9)]
            game_on = True
        else:
            game_on = False
            print('Thank you for playing Tic Tac Toe')

    # This is to switch player positions
    if player_turn == 0:
        player_turn = 1
    else:
        player_turn = 0