



# Function to read user intake and call subsequent functions
# to perform actions on the board, depending on user response
def user_resp(char, board):
    if char == 'a':
        return left_alg(board)
    elif char == 'd':
        return right_alg(board)
    elif char == 'w':
        return up_alg(board)
    elif char == 's':
        return down_alg(board)


# Functions to perform shifts on the game board, depending on user input:

# Function to perform left shift on the board
def left_alg(board):
    for a in board:
        if a[0] == a[1]:
            a[0] *= 2
            if a[2] == a[3]:
                a[1] = a[2] * 2
                a[2] = a[3] = 0
            else:
                a[1] = a[2]
                a[2] = a[3]
                a[3] = 0
    return board


# Function to perform left shift on the board
def right_alg(board):
    for a in board:
        if a[3] == a[2]:
            a[3] *= 2
            if a[0] == a[1]:
                a[2] = a[1] * 2
                a[1] = a[2] = 0
            else:
                a[2] = a[1]
                a[1] = a[0]
                a[3] = 0
    return board


# Function to perform left shift on the board
def up_alg(board):
    return board


# Function to perform left shift on the board
def down_alg(board):
    return board