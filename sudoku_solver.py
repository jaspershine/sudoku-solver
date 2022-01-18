#Sudoku solver. Written by Jasper Shine

import ast #used for converting string of 2-d list into a normal 2-d list. Source: https://stackoverflow.com/questions/19723911/convert-a-string-2d-list-back-to-2d-list-in-python
import copy


"""
The main solving function for the game.
Input: board - a 2-d array representing the game board. Must be a 9x9 board
Return value: completed board if inputted board is solvable and False otherwise
"""
def solve(board):
    empty_position = find_empty_position(board)
    # if there is not an empty position then that means we've reached the end and can return the board
    if empty_position:
        x, y = empty_position
    else:
        return board #basically returning True

    for value in range(1, len(board)+1):
        if valid_placement(board, x, y, value):
            board[y][x] = value

            # Recurse using this new value. If it is valid this will eventually return True.
            # If not, we change it back to 0 and try the next value
            if solve(board):
                return solve(board)
            board[y][x] = 0

    # If we reach this point it means there are no valid values for this postion so we return false to begin backtracking
    return False

"""
Checks if assigning a certain value at certain coordiantes of the board is valid according to the rules of sudoku.
Input: board - a 2-d array representing the game board. Must be a 9x9 board
Input: x, y - the x and y coordiantes on the board
Input: value - the value that we are checking is valid
Return value: True if value is valid at that position and False otherwise
"""
def valid_placement(board, x, y, value):
    # check the row and column of the coordinates
    boardSize = len(board)
    for other_coordinate in range(boardSize):
        if board[y][other_coordinate] == value or board[other_coordinate][x] == value:
            return False

    # check the subgrid of the current coordinates
    x_subgrid = x//3
    y_subgrid = y//3
    for i in range(y_subgrid*3, y_subgrid*3 + 3):
        for j in range(x_subgrid*3, x_subgrid*3 + 3):
            if board[i][j] == value and i != y and j != x:
                return False
    return True

"""
Finds the first empty postion on the board
Input: board - a 2-d array representing the game board. Must be a 9x9 board
Return value: x and y coordiantes of the first empty postion if one exists (0 otherwise)
"""
def find_empty_position(board):
    boardSize = len(board)
    for y in range(boardSize):
        for x in range(boardSize):
            if board[y][x] == 0:
                return (x, y)
    return 0

"""
Checks if the inputted board is in the correct format.
Input: board - a 2-d array representing the game board. Must be a 9x9 board
Return value: True if input format is valid and False otherwise
"""
def valid_inputted_board(board):
    if type(board) != type([[5, 6], [1, 2]]):
        print('Type Error: Make sure input is a 2-d list', end='\n')
        return False
    if len(board) != 9:
        print('Length Error: Make sure each list is of length 9', end='\n')
        return False
    for inner_list in board:
        if type(inner_list) != type([1, 2]):
            print('Type Error: Make sure input is a 2-d list', end='\n')
            return False
        if len(inner_list) != 9:
            print('Length Error: Make sure each list is of length 9', end='\n')
            return False
        for number in inner_list:
            if type(number) != type(5):
                print('Type Error: Make sure each value is an integer', end='\n')
                return False
            if number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('Value Error: Make sure each value is between 0-9', end='\n')
                return False

    # check if the placement of values are valid
    for y in range(9):
        for x in range(9):
            value = board[y][x]
            if value != 0:
                board_copy = copy.deepcopy(board)
                board_copy[y][x] = 0
                if not valid_placement(board_copy, x, y, value):
                    print("Invalid Input. Make sure input board follows the rules of sudoku", end='\n')
                    return False
    return True


"""
Prints the board in a nice format
"""
def print_board(board):
    for row_number in range(len(board)):
        if row_number % 3 == 0:
            print("- - - - - - - - - - - - - - -")
        for col_number in range(len(board)):
            if col_number % 3 == 0:
                print(" | ", end="")

            if col_number == 8:
                print(str(board[row_number][col_number]) + " |", end='\n')
            else:
                print(str(board[row_number][col_number]) + " ", end="")
    print('', end='\n')



if __name__ == "__main__":
    while True:
        print("SUDOKU SOLVER", end='\n')

        board_dict = {'1': [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                            [6, 8, 0, 0, 7, 0, 0, 9, 0],
                            [1, 9, 0, 0, 0, 4, 5, 0, 0],
                            [8, 2, 0, 1, 0, 0, 0, 4, 0],
                            [0, 0, 4, 6, 0, 2, 9, 0, 0],
                            [0, 5, 0, 0, 0, 3, 0, 2, 8],
                            [0, 0, 9, 3, 0, 0, 0, 7, 4],
                            [0, 4, 0, 0, 5, 0, 0, 3, 6],
                            [7, 0, 3, 0, 1, 8, 0, 0, 0]],

                        '2': [[0, 0, 0, 6, 0, 0, 4, 0, 0],
                            [7, 0, 0, 0, 0, 3, 6, 0, 0],
                            [0, 0, 0, 0, 9, 1, 0, 8, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 5, 0, 1, 8, 0, 0, 0, 3],
                            [0, 0, 0, 3, 0, 6, 0, 4, 5],
                            [0, 4, 0, 2, 0, 0, 0, 6, 0],
                            [9, 0, 3, 0, 0, 0, 0, 0, 0],
                            [0, 2, 0, 0, 0, 0, 1, 0, 0]],

                        '3': [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                            [6, 0, 0, 1, 9, 5, 0, 0, 0],
                            [0, 9, 8, 0, 0, 0, 0, 6, 0],
                            [8, 0, 0, 0, 6, 0, 0, 0, 3],
                            [4, 0, 0, 8, 0, 3, 0, 0, 1],
                            [7, 0, 0, 0, 2, 0, 0, 0, 6],
                            [0, 6, 0, 0, 0, 0, 2, 8, 0],
                            [0, 0, 0, 4, 1, 9, 0, 0, 5],
                            [0, 0, 0, 0, 8, 0, 0, 7, 9]],

                        '4': [[0, 9, 0, 0, 0, 6, 0, 4, 0],
                            [0, 0, 5, 3, 0, 0, 0, 0, 8],
                            [0, 0, 0, 0, 7, 0, 2, 0, 0],
                            [0, 0, 1, 0, 5, 0, 0, 0, 3],
                            [0, 6, 0, 0, 0, 9, 0, 7, 0],
                            [2, 0, 0, 0, 8, 4, 1, 0, 0],
                            [0, 0, 3, 0, 1, 0, 0, 0, 0],
                            [8, 0, 0, 0, 0, 2, 5, 0, 0],
                            [0, 5, 0, 4, 0, 0, 0, 8, 0]],

                        '5': [[0, 2, 0, 5, 0, 1, 0, 9, 0],
                            [8, 0, 0, 2, 0, 3, 0, 0, 6],
                            [0, 3, 0, 0, 6, 0, 0, 7, 0],
                            [0, 0, 1, 0, 0, 0, 6, 0, 0],
                            [5, 4, 0, 0, 0, 0, 0, 1, 9],
                            [0, 0, 2, 0, 0, 0, 7, 0, 0],
                            [0, 9, 0, 0, 3, 0, 0, 8, 0],
                            [2, 0, 0, 8, 0, 4, 0, 0, 7],
                            [0, 1, 0, 9, 0, 7, 0, 6, 0]],

                        '6': [[0, 2, 6, 0, 3, 0, 0, 0, 8],
                            [9, 0, 0, 6, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 1, 9, 0, 4, 0],
                            [0, 0, 7, 3, 0, 2, 0, 0, 0],
                            [0, 0, 4, 0, 7, 0, 8, 0, 0],
                            [0, 0, 0, 8, 0, 6, 7, 0, 0],
                            [0, 5, 0, 7, 2, 0, 0, 0, 0],
                            [0, 0, 9, 0, 0, 5, 0, 0, 4],
                            [4, 0, 0, 0, 6, 0, 2, 1, 0]],

                        '7': [[0, 9, 1, 0, 7, 0, 0, 0, 0],
                            [2, 0, 3, 0, 0, 0, 0, 5, 0],
                            [0, 0, 0, 4, 0, 2, 9, 0, 7],
                            [0, 0, 2, 8, 0, 6, 0, 0, 9],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [9, 0, 0, 1, 0, 4, 6, 0, 0],
                            [1, 0, 5, 2, 0, 7, 0, 0, 0],
                            [0, 8, 0, 0, 0, 0, 5, 0, 1],
                            [0, 0, 0, 0, 1, 0, 7, 6, 0]],

                        '8': [[0, 0, 1, 3, 0, 2, 0, 0, 0],
                            [0, 0, 3, 0, 0, 7, 0, 4, 5],
                            [0, 0, 7, 0, 0, 0, 0, 0, 9],
                            [0, 0, 6, 5, 0, 0, 0, 7, 0],
                            [2, 0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 9, 0, 0, 0, 1, 4, 0, 0],
                            [5, 0, 0, 0, 0, 0, 9, 0, 0],
                            [6, 1, 0, 2, 0, 0, 8, 0, 0],
                            [0, 0, 0, 9, 0, 8, 5, 0, 0]],

                        '9': [[5, 0, 9, 4, 0, 0, 0, 0, 0],
                            [0, 0, 3, 0, 0, 0, 6, 9, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0, 5],
                            [0, 5, 0, 1, 8, 0, 0, 0, 0],
                            [3, 0, 0, 0, 5, 0, 0, 0, 7],
                            [0, 0, 0, 0, 9, 6, 0, 5, 0],
                            [9, 0, 0, 0, 0, 0, 0, 7, 0],
                            [0, 3, 8, 0, 0, 0, 5, 0, 0],
                            [0, 0, 0, 0, 0, 7, 1, 0, 3]],

                }

        for key in board_dict.keys():
            print("BOARD " + key, end='\n')
            print_board(board_dict[key])
        board_number = input("Please select which board you would like to be solved [1-9] or type '0' to input your own board or type 'E' to exit: ")
        if board_number == '0':
            while True:
                inputted_board = ast.literal_eval(input("Please input board as a 2-d (9x9) list. Please only use integers from 1-9 and make sure no two values in one row, column, or subregion are the same. Represent all blank spaces as a 0: "))
                if valid_inputted_board(inputted_board):
                    print("Calculating...")
                    answer = solve(inputted_board)
                    if not answer:
                        print("No valid solution exists.")
                    else:
                        print_board(answer)
                else:
                    print("Invalid format. ")
                break
        elif board_number in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Calculating...")
            print_board(solve(board_dict[board_number]))
        elif board_number == 'E' or board_number == 'e':
            break
        else:
            print("Invalid choice")

        follow_up = input("Continue? [Y/N]: ")
        if follow_up != 'Y' and follow_up != 'y' and follow_up.lower() != 'yes':
            break
