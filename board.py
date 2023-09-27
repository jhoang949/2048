# importing files
import random


# Function to initialize the game board as a multidimensional array
def start_game():
    # initialize empty 2d game board
    board = []
    for i in range(4):
        board.append([0] * 4)
    # append starting 2's
    board[random.randrange(4)][random.randrange(4)] = 2
    board[random.randrange(4)][random.randrange(4)] = 2
    return board


# Function to print current board
def print_board(board):
    for i in board:
        print(i)
