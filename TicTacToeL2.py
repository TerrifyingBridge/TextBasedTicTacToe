import os

class Board:

    def __init__(self):
        self.board = [ [ [" "], [" "], [" "] ], [ [" "], [" "], [" "] ], [ [" "], [" "], [" "] ] ]
        self.won_x = False
        self.won_o = False

    def print_board(self):
        tot = ["","",""]
        for j in range(len(self.board)):
            tot[j] = str(self.board[j][0]) + "  " + str(self.board[j][1]) + "  " + str(self.board[j][2])
        return tot

    def check_space(self, move):
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        if (self.board[row][col][0] == " "):
            return True
        else:
            return False

    def check_win_row(self, row_num):
        if (self.board[row_num][0][0] == self.board[row_num][1][0] and self.board[row_num][1][0] == self.board[row_num][2][0]):
            return True
        else:
            return False

    def check_win_col(self, col_num):
        if (self.board[0][col_num][0] == self.board[1][col_num][0] and self.board[1][col_num][0] == self.board[2][col_num][0]):
            return True
        else:
            return False

    def check_win_diag1(self):
        if (self.board[0][0][0] == self.board[1][1][0] and self.board[1][1][0] == self.board[2][2][0]):
            return True
        else:
            return False

    def check_win_diag2(self):
        if (self.board[0][2][0] == self.board[1][1][0] and self.board[1][1][0] == self.board[2][0][0]):
            return True
        else:
            return False

    def check_game(self):
        for j in range(0,3):
            if (self.check_win_row(j) == True and (self.board[j][0][0] == "X" or self.board[j][0][0] == "O")):
                if (self.board[j][0][0] == "X"):
                    self.won_x = True
                else:
                    self.won_o = True
                return (self.won_x, self.won_o)
            elif (self.check_win_col(j) == True and (self.board[0][j][0] == "X" or self.board[0][j][0] == "O")):
                if (self.board[0][j][0] == "X"):
                    self.won_x = True
                else:
                    self.won_o = True
                return (self.won_x, self.won_o)
            elif ((self.check_win_diag1() == True or self.check_win_diag2() == True) and (self.board[1][1][0] == "X" or self.board[1][1][0] == "O")):
                if (self.board[1][1][0] == "X"):
                    self.won_x = True
                else:
                    self.won_o = True
                return (self.won_x, self.won_o)
        else:
            return (self.won_x, self.won_o)

    def get_win_x(self):
        return self.won_x

    def get_win_o(self):
        return self.won_o

    def place_x(self, move):
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        self.board[row][col][0] = "X"
        return

    def place_o(self, move):
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        self.board[row][col][0] = "O"
        return

    def make_xo(self, i):
        if (i % 2 == 0):
            for row in self.board:
                for space in row:
                    space[0] = "X"
        else:
            for row in self.board:
                for space in row:
                    space[0] = "O"

b1 = Board()
b2 = Board()
b3 = Board()
b4 = Board()
b5 = Board()
b6 = Board()
b7 = Board()
b8 = Board()
b9 = Board()

main_slate = [ [b1, b2, b3], [b4, b5, b6], [b7, b8, b9] ]

def print_slate(slate):
    a = 0
    for row in slate:
        board1 = row[0].print_board()
        board2 = row[1].print_board()
        board3 = row[2].print_board()

        for k in range(0,3):
            print(board1[k] + " | " + board2[k] + " | " + board3[k])
        if (a < 2):
            print("--------------------+---------------------+--------------------")
            a += 1
    return

def check_board(slate, move):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if (slate[row][col].get_win_x() or slate[row][col].get_win_o()):
        return False
    else:
        return True

def s_check_win_row(slate, row_num):
    if ( ((slate[row_num][0].get_win_x() == True) and (slate[row_num][1].get_win_x() == True) and (slate[row_num][2].get_win_x() == True)) or ((slate[row_num][0].get_win_o() == True) and (slate[row_num][1].get_win_o() == True) and (slate[row_num][2].get_win_o() == True))):
        return True
    else:
        return False

def s_check_win_col(slate, col_num):
    if (((slate[0][col_num].get_win_x() == True) and (slate[1][col_num].get_win_x() == True) and (slate[2][col_num].get_win_x() == True)) or ((slate[0][col_num].get_win_o() == True) and (slate[1][col_num].get_win_o() == True) and (slate[2][col_num].get_win_o() == True))):
        return True
    else:
        return False

def s_check_win_diag1(slate):
    if (((slate[0][0].get_win_x() == True) and (slate[1][1].get_win_x() == True) and (slate[2][2].get_win_x() == True)) or ((slate[0][0].get_win_o() == True) and (slate[1][1].get_win_o() == True) and (slate[2][2].get_win_o() == True))):
        return True
    else:
        return False

def s_check_win_diag2(slate):
    if (((slate[0][2].get_win_x() == True) and (slate[1][1].get_win_x() == True) and (slate[0][2].get_win_x() == True)) or ((slate[0][2].get_win_o() == True) and (slate[1][1].get_win_o() == True) and (slate[0][2].get_win_o() == True))):
        return True
    else:
        return False

def check_game(slate, move, i):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    slate[row][col].check_game()
    #print(slate[row][col].check_game())
    if ((slate[row][col].get_win_x()) or (slate[row][col].get_win_o())):
        slate[row][col].make_xo(i)

    for k in range(0,3):
        if ((s_check_win_row(slate, k) == True)):
            return False
        elif ((s_check_win_col(slate, k) == True)):
            return False
        elif ((s_check_win_diag1(slate) == True) or (s_check_win_diag2(slate) == True)):
            return False
    return True

def check_input(move):
    try:
        temp = int(move)
        if ((0 < temp) and (temp < 10)):
            return temp
        else:
            return -1
    except:
        return -1

game = True
cur_move1 = 0
i = 0
while(game):
    os.system("cls")
    print_slate(main_slate)
    if (i % 2 == 0):
        print("It is Player X's turn")
    else:
        print("It is Player O's turn")
    print("You are playing in board " + str(cur_move1)) 
    if (cur_move1 == 0 or cur_move1 == -1):
        cur_move1 = input("Please Choose Your Board: ")
        cur_move2 = input("Please Choose Your Space: ")
        cur_move1 = check_input(cur_move1)
        cur_move2 = check_input(cur_move2)
    else:
        cur_move2 = input("Please Choose Your Space: ")
        cur_move2 = check_input(cur_move2)
    cur_move = [int(cur_move1), int(cur_move2)]
    #print(cur_move)
    s_row = int((cur_move[0] - 1) / 3)
    s_col = (cur_move[0] - 1) % 3
    #print(s_row, " ", s_col)
    if (cur_move1 == -1 or cur_move2 == -1):
        os.system("cls")
        print("Try Again")
    elif (main_slate[s_row][s_col].check_space(cur_move[1])):
        if (i % 2 == 0):
            main_slate[s_row][s_col].place_x(cur_move[1])
        else:
            main_slate[s_row][s_col].place_o(cur_move[1])

        game = check_game(main_slate, cur_move[0], i)

        if (check_board(main_slate, cur_move[1])):
            cur_move1 = cur_move2
        else:
            cur_move1 = 0        
        i += 1
        os.system("cls")
    else:
        os.system("cls")
        print("Try Again")

print_slate(main_slate)
if ((i - 1) % 2 == 0):
    print("Congrats! Player X Won!")
else:
    print("Congratgs! Player 0 Won!")
    print("Won in " + str(i + 2) + " moves.")
