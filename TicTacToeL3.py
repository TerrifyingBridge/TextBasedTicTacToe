import os

########################################################
#############        Game Set Up        ################
########################################################

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
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
                return (self.won_x, self.won_o)
            elif (self.check_win_col(j) == True and (self.board[0][j][0] == "X" or self.board[0][j][0] == "O")):
                if (self.board[0][j][0] == "X"):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
                return (self.won_x, self.won_o)
            elif ((self.check_win_diag1() == True or self.check_win_diag2() == True) and (self.board[1][1][0] == "X" or self.board[1][1][0] == "O")):
                if (self.board[1][1][0] == "X"):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
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

class Slate:

    def __init__(self):
        self.b1 = Board()
        self.b2 = Board()
        self.b3 = Board()
        self.b4 = Board()
        self.b5 = Board()
        self.b6 = Board()
        self.b7 = Board()
        self.b8 = Board()
        self.b9 = Board()

        self.slate = [ [self.b1, self.b2, self.b3], [self.b4, self.b5, self.b6], [self.b7, self.b8, self.b9] ]
        self.won_x = False
        self.won_o = False
    
    def print_slate(self):
        tot = [ [[], [], []], [[], [], []], [[], [], []] ]

        for k in range(len(self.slate)):
            for l in range(len(self.slate[k])):
                tot[k][l] = self.slate[k][l].print_board()
        return tot

    def check_board(self, move):
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        if (self.slate[row][col].get_win_x() or self.slate[row][col].get_win_o()):
            return False
        else:
            return True

    def check_space(self, move):
        s_row = int((move[0] - 1) / 3)
        s_col = (move[0] - 1) % 3
        if (self.slate[s_row][s_col].check_space(move[1])):
            return True
        else:
            return False

    def check_win_row(self, row_num):
        if ( ((self.slate[row_num][0].get_win_x() == True) and
             (self.slate[row_num][1].get_win_x() == True) and
             (self.slate[row_num][2].get_win_x() == True)) or
             ((self.slate[row_num][0].get_win_o() == True) and
             (self.slate[row_num][1].get_win_o() == True) and
             (self.slate[row_num][2].get_win_o() == True)) ):
            return True
        else:
            return False

    def check_win_col(self, col_num):
        if ( ((self.slate[0][col_num].get_win_x() == True) and
             (self.slate[1][col_num].get_win_x() == True) and
             (self.slate[2][col_num].get_win_x() == True)) or
             ((self.slate[0][col_num].get_win_o() == True) and
             (self.slate[1][col_num].get_win_o() == True) and
             (self.slate[2][col_num].get_win_o() == True)) ):
            return True
        else:
            return False

    def check_win_diag1(self):
        if (((self.slate[0][0].get_win_x() == True) and
             (self.slate[1][1].get_win_x() == True) and
             (self.slate[2][2].get_win_x() == True)) or
            ((self.slate[0][0].get_win_o() == True) and
             (self.slate[1][1].get_win_o() == True) and
             (self.slate[2][2].get_win_o() == True))):
            return True
        else:
            return False

    def check_win_diag2(self):
        if (((self.slate[2][0].get_win_x() == True) and
             (self.slate[1][1].get_win_x() == True) and
             (self.slate[0][2].get_win_x() == True)) or
            ((self.slate[2][0].get_win_o() == True) and
             (self.slate[1][1].get_win_o() == True) and
             (self.slate[0][2].get_win_o() == True))):
            return True
        else:
            return False

    def check_game(self):
        for row in self.slate:
            for board in row:
                dummy = board.check_game()
        
        for k in range(0,3):
            if (self.check_win_row(k) == True and (self.slate[k][0].get_win_x() or self.slate[k][0].get_win_o())):
                if (self.slate[k][0].get_win_x()):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
            elif (self.check_win_col(k) == True and (self.slate[0][k].get_win_x() or self.slate[0][k].get_win_o())):
                if (self.slate[0][k].get_win_x()):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
            elif ((self.check_win_diag1() == True or self.check_win_diag2() == True) and (self.slate[1][1].get_win_x() or self.slate[1][1].get_win_o())):
                if (self.slate[1][1].get_win_x()):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
        return

    def get_win_x(self):
        return self.won_x

    def get_win_o(self):
        return self.won_o

    #Make sure move is a two dimensional vector
    def place_x(self, move):
        row = int((move[0] - 1) / 3)
        col = (move[0] - 1) % 3
        self.slate[row][col].place_x(move[1])
        return

    def place_o(self, move):
        row = int((move[0] - 1) / 3)
        col = (move[0] - 1) % 3
        self.slate[row][col].place_o(move[1])
        return
    
    def make_xo(self, i):
        if (i % 2 == 0):
            for row in self.slate:
                for board in row:
                    board.make_xo(i)
        else:
            for row in self.slate:
                for board in row:
                    board.make_xo(i)
        return

s1 = Slate()
s2 = Slate()
s3 = Slate()
s4 = Slate()
s5 = Slate()
s6 = Slate()
s7 = Slate()
s8 = Slate()
s9 = Slate()

main_table = [ [s1, s2, s3], [s4, s5, s6], [s7, s8, s9] ]

def print_table(table):
    a = 0
    b = 0
    for row in table:
        slate1 = row[0].print_slate()
        slate2 = row[1].print_slate()
        slate3 = row[2].print_slate()

        for m in range(0,3):
            for n in range(0,3):
                print(slate1[m][0][n] + " | " + slate1[m][1][n] + " | " + slate1[m][2][n] + "  ||  "
                    + slate2[m][0][n] + " | " + slate2[m][1][n] + " | " + slate2[m][2][n] + "  ||  "
                    + slate3[m][0][n] + " | " + slate3[m][1][n] + " | " + slate3[m][2][n])
            if (b < 2):
                print("--------------------+---------------------+--------------------" + "  ||  "
                      + "--------------------+---------------------+--------------------" + "  ||  "
                      + "--------------------+---------------------+--------------------")
                b += 1
        b = 0
        if (a < 2):
            print("=========================================================================================================================================================================================================")
            a += 1
    return

def check_slate(table, move):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if (table[row][col].get_win_x() or table[row][col].get_win_o()):
        return False
    else:
        return True

def t_check_win_row(table, row_num):
    if ( ((table[row_num][0].get_win_x() == True) and
          (table[row_num][1].get_win_x() == True) and
          (table[row_num][2].get_win_x() == True)) or
         ((table[row_num][0].get_win_o() == True) and
          (table[row_num][1].get_win_o() == True) and
          (table[row_num][2].get_win_o() == True)) ):
        return True
    else:
        return False

def t_check_win_col(table, col_num):
    if ( ((table[0][col_num].get_win_x() == True) and
          (table[1][col_num].get_win_x() == True) and
          (table[2][col_num].get_win_x() == True)) or
         ((table[0][col_num].get_win_o() == True) and
          (table[1][col_num].get_win_o() == True) and
          (table[2][col_num].get_win_o() == True)) ):
        return True
    else:
        return False
    

def t_check_win_diag1(table):
    if (((table[0][0].get_win_x() == True) and
         (table[1][1].get_win_x() == True) and
         (table[2][2].get_win_x() == True)) or
        ((table[0][0].get_win_o() == True) and
         (table[1][1].get_win_o() == True) and
         (table[2][2].get_win_o() == True))):
        return True
    else:
        return False

def t_check_win_diag2(table):
    if (((table[2][0].get_win_x() == True) and
         (table[1][1].get_win_x() == True) and
         (table[0][2].get_win_x() == True)) or
        ((table[2][0].get_win_o() == True) and
         (table[1][1].get_win_o() == True) and
         (table[0][2].get_win_o() == True))):
        return True
    else:
        return False

def check_game(table, move, i):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    table[row][col].check_game()
    if ((table[row][col].get_win_x()) or (table[row][col].get_win_o())):
        table[row][col].make_xo(i)

    for m in range(0,3):
        if ((t_check_win_row(table, m) == True)):
            return False
        elif ((t_check_win_col(table, m) == True)):
            return False
        elif ((t_check_win_diag1(table) == True) or (t_check_win_diag2(table) == True)):
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

#########################################################
##############   AI Functions Below    ##################
#########################################################



###################################################
##############     Main Game      #################
###################################################

i = 0
game = True
cur_move1 = 0
cur_move2 = 0
pre_move = [0, 0, 0]
os.system("cls")
while(game):
    print_table(main_table)
    if (i % 2 == 0):
        print("It is Player X's Turn")
    else:
        print("It is Player O's Turn")
    print("You are playing in Slate " + str(cur_move1))
    print("You are playing in Board " + str(cur_move2))
    if (cur_move1 == 0 or cur_move1 == -1):
        cur_move1 = input("Please Choose Your Slate: ")
        cur_move2 = input("Please Choose Your Board: ")
        cur_move3 = input("Please Choose Your Space: ")
        cur_move1 = check_input(cur_move1)
        cur_move2 = check_input(cur_move2)
        cur_move3 = check_input(cur_move3)
    elif (cur_move1 != 0 and (cur_move2 == 0 or cur_move2 == -1)):
        cur_move2 = input("Please Choose Your Board: ")
        cur_move3 = input("Please Choose Your Space: ")
        cur_move2 = check_input(cur_move2)
        cur_move3 = check_input(cur_move3)
    else:
        cur_move3 = input("Please Choose Your Space: ")
        cur_move3 = check_input(cur_move3)
    cur_move = [int(cur_move1), int(cur_move2), int(cur_move3)]
    t_row = int((cur_move[0] - 1) / 3)
    t_col = (cur_move[0] - 1) % 3
    s_row = int((cur_move[1] - 1) / 3)
    s_col = (cur_move[1] - 1) % 3
    if (cur_move1 == -1 or cur_move2 == -1 or cur_move3 == -1):
        os.system("cls")
        print("Try Again")
    elif (main_table[t_row][t_col].check_space([cur_move[1],cur_move[2]]) and
          main_table[t_row][t_col].check_board(cur_move[1]) and
          check_slate(main_table, cur_move[0])):
        #print(cur_move)
        #print(t_row, t_col)
        if (i % 2 == 0):
            main_table[t_row][t_col].place_x([cur_move[1],cur_move[2]])
        else:
            main_table[t_row][t_col].place_o([cur_move[1],cur_move[2]])

        game = check_game(main_table, cur_move[0], i)

        if (check_slate(main_table, cur_move[1])):
            if (main_table[s_row][s_col].check_board(cur_move[2])):
                print(main_table[t_row][t_col].check_board(cur_move[2]))
                cur_move1 = cur_move2
                cur_move2 = cur_move3
            else:
                cur_move1 = cur_move2
                cur_move2 = 0
        else:
            cur_move1 = 0
        i += 1
        os.system("cls")
    elif (not check_slate(main_table, cur_move[0])):
        cur_move1 = 0
        os.system("cls")
        print("Try Again")
    elif (not main_table[t_row][t_col].check_board(cur_move[1])):
        cur_move2 = 0
        os.system("cls")
        print("Try Again")
    else:
        os.system("cls")
        print("Try Again")

print_table(main_table)
if ((i - 1) % 2 == 0):
    print("Congrats! Player X Won!")
else:
    print("Congrats! Player O Won!")
print("Won in " + str(i + 2) + " moves.")