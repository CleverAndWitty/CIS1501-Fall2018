def game_over(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def win_horizontaly(board, player):
    # FIXME
    return False


def win_diagonally_up(board, player):
    # FIXME
    return False


def win_diagonally_down(board, player):
    # FIXME
    return False


def win(board, player):
    return win_horizontaly(board, player) \
        or win_diagonally_up(board, player) \
        or win_diagonally_down(board, player)


def place_piece(board, player):
    print("{}'s turn!:".format(player))
    row = int(input("What column do you want to play?"))
    #...


def print_board(board):
    for row in board:
        print(row)


board = []
for row in range(6):
    board.append([])
    for column in range(7):
        board[row].append(" ")


print_board(board)
active_player = 'X'

while not game_over(board):
    place_piece(board, active_player)
    if win(active_player):
        print("{} wins!".format(active_player))
        break
    else:
        if active_player == 'X':
            active_player = 'O'
        else:
            active_player = 'X'
