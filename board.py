# importing files
import random

class Board:
    # initialize empty 2d game board
    def __init__(self):
        self.board = []
        for i in range(4):
            self.board.append([0] * 4)
        # append starting 2's on the board
        self.board[random.randrange(4)][random.randrange(4)] = 2
        self.board[random.randrange(4)][random.randrange(4)] = 2

    # Function to create random 2's and 4's when action is made
    def gen_squares(self):
        # Iterate the board and collect empty positions
        empty = []
        for x in range(4):
            for y in range(4):
                if self.board[x][y] == 0:
                    empty.append([x, y])
        # Generate random numbers (90% chance a 2 and 10% chance a 4) and adds to board
        if random.random() > 0.89:
            num = 4
        else:
            num = 2

        # If there are empty positions, the new square is generated
        # Otherwise, call check_game() to see if the game is over
        if len(empty) == 0:
            self.check_game()
        else:
            rand_pos = empty[random.randrange(len(empty))]
            self.board[rand_pos[0]][rand_pos[1]] = num


    # Function to check the board if the game is over when the board is filled
    # INCOMPLETE
    def check_game(self):
        self.lose_game()

    # Function to call to end game
    # INCOMPLETE
    def lose_game():
        print("Game Over!")


    # Function to print current board
    def print_board(self):
        for i in self.board:
            print(i)
