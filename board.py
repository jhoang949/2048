# importing files
import random


# Function to initialize the game board as a multidimensional array
def start_game():
    # initialize empty 2d game board
    board = []
    for i in range(4):
        board.append([0] * 4)
    # append starting 2's on the board
    board[random.randrange(4)][random.randrange(4)] = 2
    board[random.randrange(4)][random.randrange(4)] = 2
    return board


# Function to create random 2's and 4's when action is made
def gen_squares(game_board):
    # Iterate the board and collect empty positions
    empty = []
    for x in range(4):
        for y in range(4):
            if game_board[x][y] == 0:
                empty.append([x, y])
    # Generate random numbers (90% chance a 2 and 10% chance a 4) and adds to board
    if random.random() > 0.89:
        num = 4
    else:
        num = 2

    # If there are empty positions, the new square is generated
    # Otherwise, call check_game() to see if the game is over
    if len(empty) == 0:
        check_game()
    else:
        rand_pos = empty[random.randrange(len(empty))]
        game_board[rand_pos[0]][rand_pos[1]] = num


# Function to check the board if the game is over when the board is filled
# INCOMPLETE
def check_game():
    lose_game()

# Function to call to end game
# INCOMPLETE
def lose_game():
    print("Game Over!")


# Function to print current board
def print_board(game_board):
    for i in game_board:
        print(i)
