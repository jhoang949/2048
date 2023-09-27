import random

def startGame():
    # initialize empty 2d game board
    board = []
    for i in range(4):
        board.append([0] * 4)
    # append starting 2's
    board[random.randrange(4)][random.randrange(4)] = 2
    board[random.randrange(4)][random.randrange(4)] = 2
    return board