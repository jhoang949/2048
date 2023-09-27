# This is a sample Python main for the project.

# imported files
import board


# Main function
if __name__ == '__main__':
    # explanation for how the game is played
    print('The commands for the game are as follows')
    print('"w" is up\n"a" is left\n"s" is down\n"d" is right\n\n')

    # initialize game board
    game_board = board.startGame()

    # print the game board
    for i in game_board:
        print(i)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
