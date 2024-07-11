from random import randrange

# SkillsForAll
# Python Essentials 1 - Final Project
# TicTacToe

size = 3
cell_width = 7
cell_height = 4

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list = []
    for row in range(size):
        for col in range(size):
            spot = board[row][col]
            if spot != 'X' and spot != 'O':
                free_list.append((row, col))
    return free_list


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    board_text = ""

    for row in board:
        board_text += ("+" + ("-" * cell_width)) * size + "+\n"

        for scanline in range(1, cell_height):
            if scanline == cell_height//2:
                for col in row:
                    board_text += "|" + " " * (cell_width // 2) + str(col) + " " * (cell_width // 2)
                board_text += "|\n"
            else:
                board_text += ("|" + (" " * cell_width)) * size + "|\n"


    board_text += ("+" + ("-" * cell_width)) * size + "+\n"

    print(board_text)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    free_list = make_list_of_free_fields(board)
    if free_list == []:
        return print("Draw")

    try:
        move = int(input("Enter your move:"))

        if move < 0 and move > 9:
            print("Spaces should be between 0 and 10")
            return enter_move(board)

        move -=1

        row = move//size
        col = move%size

        if (row, col) not in free_list:
            print("Space already taken, enter another space")
            return enter_move(board)

        board[row][col] = 'O'
    except:
        print("Invalid move")
        return enter_move(board)

    if victory_for(board, 'O') == False:
        draw_move(board)
    else:
        print("You won")



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    combos = [(), (), ()]

    for row in range(size):
        for col in range(size):
            combos[col] += (board[row][col],)

        combos.append(tuple(board[row]))

    if sign == 'X':
        combos.append((board[0][0], board[1][1], board[2][2]))
        combos.append((board[2][0], board[1][1], board[0][2]))

    return (sign, sign, sign) in combos

def draw_move(board):
    # The function draws the computer's move and updates the board.

    free_list = make_list_of_free_fields(board)

    if free_list == []:
        return print("Draw")

    row = 1
    col = 1

    while((row, col) not in free_list):
        move = randrange(size*size)
        row = move//size
        col = move%size

    board[row][col] = 'X'

    display_board(board)

    if victory_for(board, 'X') == False:
        enter_move(board)
    else:
        print("Computer won")


board = [[1 + row * size + col for col in range(size)] for row in range(size)]

draw_move(board)
