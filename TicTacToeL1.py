import numpy as np
import os

full_board = [ [ [" "], [" "], [" "] ], [ [" "], [" "], [" "] ], [ [" "], [" "], [" "] ] ]

def print_board(board):
    for row in board:
        print (str(row[0]) + "  " + str(row[1]) + "  " + str(row[2]))
    return

def check_move(board, move):
    row = int((move - 1)/3)
    col = (move - 1) % 3
    if (board[row][col][0] == " " ):
        return True
    else:
        return False

def check_win_row(board, row_num):
    if (board[row_num][0][0] == board[row_num][1][0] and board[row_num][1][0] == board[row_num][2][0]):
        return True
    else:
        return False

def check_win_col(board, col_num):
    if (board[0][col_num][0] == board[1][col_num][0] and board[1][col_num][0] == board[2][col_num][0]):
        return True
    else:
        return False

def check_win_diag1(board):
    if (board[0][0][0] == board[1][1][0] and board[1][1][0] == board[2][2][0]):
        return True
    else:
        return False
def check_win_diag2(board):
    if (board[0][2][0] == board[1][1][0] and board[1][1][0] == board[2][0][0]):
        return True
    else:
        return False
def check_game(board):
    for j in range(0,3):
        if (check_win_row(board, j) == True and (board[j][0][0] == "X" or board[j][0][0] == "O")):
            return False
        elif (check_win_col(board, j) == True and (board[0][j][0] == "X" or board[0][j][0] == "O")):
            return False
        elif ((check_win_diag1(board) == True or check_win_diag2(board) == True) and (board[1][1][0] == "X" or board[1][1][0] == "O")):
            return False
    return True
game = True
i = 0
os.system('cls')
while(game):
    print_board(full_board)
    cur_move = input("Please Choose Your Square: ")
    cur_move = int(cur_move)
    #print (cur_move)
    if (check_move(full_board, cur_move)):
        row = int((cur_move - 1) / 3)
        col = (cur_move - 1) % 3
        if (i % 2 == 0):
            full_board[row][col][0] = "X"
        else:
            full_board[row][col][0] = "O"
        game = check_game(full_board)
        i += 1
        os.system('cls')
    else:
        os.system('cls')
        print("Try Again")


print_board(full_board)
if ((i - 1)% 2 == 0):
    print("Congrats! Player X Won!")
else:
    print("Congrats! Player O Won!")
    
    
