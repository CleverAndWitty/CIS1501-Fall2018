def game_over(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def win_horizontaly(board, player):
    for row in board:
        for column in range(4):
            if row[column] == player \
                    and row[column+1] == player \
                    and row[column+2] == player \
                    and row[column+3] == player:
                return True
    return False


def win_diagonally_up(board, player):
    for row in range(3,6):
        for column in range(4):
            if board[row][column] == player \
                    and board[row - 1][column + 1] == player \
                    and board[row - 2][column + 2] == player \
                    and board[row - 3][column + 3] == player:
                return True
    return False


def win_diagonally_down(board, player):
    for row in range(3):
        for column in range(4):
            if board[row][column] == player \
                    and board[row + 1][column + 1] == player \
                    and board[row + 2][column + 2] == player \
                    and board[row + 3][column + 3] == player:
                return True
    return False

def win_vertically(board, player):
    for row in range(3):
        for column in range(7):
            if board[row][column] == player \
                    and board[row + 1][column] == player \
                    and board[row + 2][column] == player \
                    and board[row + 3][column] == player:
                return True
    return False


def win(board, player):
    return win_horizontaly(board, player) \
        or win_diagonally_up(board, player) \
        or win_diagonally_down(board, player) \
        or win_vertically(board, player)


def place_piece(board, player):
    print("{}'s turn!:".format(player))
    while True:
        column = int(input("What column do you want to play?"))
        for row in range(5,-1,-1):
            if board[row][column] == " ":
                board[row][column] = player
                return
        print("You can not play in that column!")



def print_board(board):
    for row in board:
        print(row)


board = []
for row in range(6):
    board.append([])
    for column in range(7):
        board[row].append(" ")


active_player = 'X'

while not game_over(board):
    print_board(board)
    place_piece(board, active_player)
    if win(board, active_player):
        print("{} wins!".format(active_player))
        break
    else:
        if active_player == 'X':
            active_player = 'O'
        else:
            active_player = 'X'
else:
    print("Tie game!")

print_board(board)
