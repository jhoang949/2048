
import board


# Function to read user intake and call subsequent functions
# to perform actions on the board, depending on user response
def user_resp(char, game_board):
    if char == 'a':
        return left_alg(game_board)
    elif char == 'd':
        return right_alg(game_board)
    elif char == 'w':
        return up_alg(game_board)
    elif char == 's':
        return down_alg(game_board)


# Functions to perform shifts on the game board, depending on user input:

# Function to perform left shift on the board
def left_alg(game_board):
    # Variable to see if the board changed in any way
    moved = False

    # Move all numbers to left if possible
    for a in game_board:
        pos = 0
        for i in range(4):
            # If square is empty, it moves on
            if a[i] == 0:
                continue
            # If square is not empty and is in the same position as the last empty position,
            # move the empty position forward and continue
            elif i == pos:
                pos += 1
            # If square is not empty and is not in the same position as last empty position,
            # move the value to the last empty position
            else:
                a[pos] = a[i]
                a[i] = 0
                pos += 1
                moved = True

    # Compresses squares if they are similar in each array
    for a in game_board:
        if a[0] == a[1] and a[0] != 0:
            a[0] *= 2
            if a[2] == a[3]:
                a[1] = a[2] * 2
                a[2] = a[3] = 0
            else:
                a[1] = a[2]
                a[2] = a[3]
                a[3] = 0
            moved = True
        elif a[1] == a[2] and a[1] != 0:
            a[1] *= 2
            a[2] = a[3]
            a[3] = 0
            moved = True
        elif a[2] == a[3] and a[2] != 0:
            a[2] *= 2
            a[3] = 0
            moved = True

    # adds square to the board if the board changed
    if moved:
        board.gen_squares(game_board)
        return game_board
    else:
        return game_board


# Function to perform right shift on the board
def right_alg(game_board):
    # Variable to see if the board changed in any way
    moved = False

    # Move all numbers to right if possible
    for a in game_board:
        pos = -1
        for i in range(1, 5):
            # If square is empty, it moves on
            if a[-i] == 0:
                continue
            # If square is not empty and is in the same position as the last empty position,
            # move the empty position forward and continue
            elif -i == pos:
                pos -= 1
                continue
            # If square is not empty and is not in the same position as last empty position,
            # move the value to the last empty position
            else:
                a[pos] = a[-i]
                a[-i] = 0
                pos -= 1
                moved = True

    # Compresses squares if they are similar in each array
    for a in game_board:
        if a[3] == a[2] and a[3] != 0:
            a[3] *= 2
            if a[0] == a[1]:
                a[2] = a[1] * 2
                a[1] = a[0] = 0
            else:
                a[2] = a[1]
                a[1] = a[0]
                a[0] = 0
            moved = True
        elif a[2] == a[1] and a[2] != 0:
            a[2] *= 2
            a[1] = a[0]
            a[0] = 0
            moved = True
        elif a[0] == a[1] and a[1] != 0:
            a[1] *= 2
            a[0] = 0
            moved = True

    # Adds square to the board if the board changed
    if moved:
        board.gen_squares(game_board)
        return game_board
    else:
        return game_board


# Function to perform up shift on the board
def up_alg(game_board):
    # Variable to see if the board changed in any way
    moved = False

    # Move all numbers up if possible
    for i in range(4):
        pos = 0
        for j in range(4):
            # If square is empty, it moves on
            if game_board[j][i] == 0:
                continue
            # If square is not empty and is in the same position as the last empty position,
            # move the empty position forward and continue
            elif j == pos:
                pos += 1
                continue
            # If square is not empty and is not in the same position as last empty position,
            # move the value to the last empty position
            else:
                game_board[pos][i] = game_board[j][i]
                game_board[j][i] = 0
                pos += 1
                moved = True

    # Compresses squares if they are similar in each array
    for i in range(4):
        if game_board[0][i] == game_board[1][i] and game_board[0][i] != 0:
            game_board[0][i] *= 2
            if game_board[2][i] == game_board[3][i]:
                game_board[1][i] = game_board[2][i] * 2
                game_board[2][i] = game_board[3][i] = 0
            else:
                game_board[1][i] = game_board[2][i]
                game_board[2][i] = game_board[3][i]
                game_board[3][i] = 0
            moved = True
        elif game_board[1][i] == game_board[2][i] and game_board[1][i] != 0:
            game_board[1][i] *= 2
            game_board[2][i] = game_board[3][i]
            game_board[3][i] = 0
            moved = True
        elif game_board[2][i] == game_board[3][i] and game_board[2][i] != 0:
            game_board[2][i] *= 2
            game_board[3][i] = 0
            moved = True

    # Adds square to the board if the board changed
    if moved:
        board.gen_squares(game_board)
        return game_board
    else:
        return game_board


# Function to perform down shift on the board
def down_alg(game_board):
    # Variable to see if the board changed in any way
    moved = False

    # Move all numbers up if possible
    for i in range(4):
        pos = -1
        for j in range(1, 5):
            # If square is empty, it moves on
            if game_board[-j][i] == 0:
                continue
            # If square is not empty and is in the same position as the last empty position,
            # move the empty position forward and continue
            elif -j == pos:
                pos -= 1
                continue
            # If square is not empty and is not in the same position as last empty position,
            # move the value to the last empty position
            else:
                game_board[pos][i] = game_board[-j][i]
                game_board[-j][i] = 0
                pos -= 1
                moved = True

    # Compresses squares if they are similar in each array
    for i in range(4):
        if game_board[3][i] == game_board[2][i] and game_board[3][i] != 0:
            game_board[3][i] *= 2
            if game_board[1][i] == game_board[0][i]:
                game_board[2][i] = game_board[1][i] * 2
                game_board[1][i] = game_board[0][i] = 0
            else:
                game_board[2][i] = game_board[1][i]
                game_board[1][i] = game_board[0][i]
                game_board[0][i] = 0
            moved = True
        elif game_board[2][i] == game_board[1][i] and game_board[2][i] != 0:
            game_board[2][i] *= 2
            game_board[1][i] = game_board[0][i]
            game_board[0][i] = 0
            moved = True
        elif game_board[1][i] == game_board[0][i] and game_board[1][i] != 0:
            game_board[1][i] *= 2
            game_board[0][i] = 0
            moved = True

    # Adds square to the board if the board changed
    if moved:
        board.gen_squares(game_board)
        return game_board
    else:
        return game_board