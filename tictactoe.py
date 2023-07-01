import random

# function to print the board


def display_board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])

# player chooses their symbol


def select_symbol():
    symbol = ''
    while not (symbol == 'X' or symbol == "O"):
        symbol = input("Choose X or O: ")
    if symbol == "X":
        return ('X', 'O')
    else:
        return ('O', 'X')

# function to place a symbol on the board


def place_symbol_onboard(board, symbol, position):
    board[position] = symbol


def check_if_win(board, symbol):
    return ((board[7] == symbol and board[8] == symbol and board[9] == symbol) or  # across the top
            (board[4] == symbol and board[5] == symbol and board[6] == symbol) or  # across the middle
            (board[1] == symbol and board[2] == symbol and board[3] == symbol) or  # across the bottom
            (board[7] == symbol and board[4] == symbol and board[1] == symbol) or  # down the middle
            (board[8] == symbol and board[5] == symbol and board[2] == symbol) or  # down the middle
            (board[9] == symbol and board[6] == symbol and board[3] == symbol) or  # down the right side
            (board[7] == symbol and board[5] == symbol and board[3] == symbol) or  # diagonal
            (board[9] == symbol and board[5] == symbol and board[1] == symbol))  # diagonal

# function to determine who should start


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# check if position is available


def space_check(board, position):
    return board[position] == ' '

# function to check if board is full


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# function to let player decide their move


def player_move(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

# function to ask if players want to keep on playing


def replay():
    return input('Do you want to play again? Enter Yes or No: ').upper().startswith('Y')


print("Welcome to Tic Tac Toe")

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_symbol, player2_symbol = select_symbol()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_move(theBoard)
            place_symbol_onboard(theBoard, player1_symbol, position)

            if check_if_win(theBoard, player1_symbol):
                display_board(theBoard)
                print('Congratulations! Player1 has won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_move(theBoard)
            place_symbol_onboard(theBoard, player2_symbol, position)

            if check_if_win(theBoard, player2_symbol):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
