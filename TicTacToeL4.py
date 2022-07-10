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

class Table:

    def __init__(self):
        self.s1 = Slate()
        self.s2 = Slate()
        self.s3 = Slate()
        self.s4 = Slate()
        self.s5 = Slate()
        self.s6 = Slate()
        self.s7 = Slate()
        self.s8 = Slate()
        self.s9 = Slate()

        self.table = [ [self.s1, self.s2, self.s3], [self.s4, self.s5, self.s6], [self.s7, self.s8, self.s9] ]
        self.won_x = False
        self.won_o = False

    def print_table(self):
        tot = [ [[], [], []], [[], [], []], [[], [], []] ]
        for k in range(len(self.table)):
            for l in range(len(self.table)):
                tot[k][l] = self.table[k][l].print_slate()
        return tot

    def check_slate(self, move):
        row = int((move - 1) / 3)
        col = (move - 1) % 3
        if (self.table[row][col].get_win_x() or self.table[row][col].get_win_o()):
            return False
        else:
            return True

    #Make sure move is a two dimensional vector
    def check_board(self, move):
        s_row = int((move[0] - 1) / 3)
        s_col = (move[0] - 1) % 3
        if (self.table[s_row][s_col].check_board(move[1])):
            return True
        else:
            return False

    #Make sure move is a three dimensional vector
    def check_space(self, move):
        row = int((move[0] - 1) / 3)
        col = (move[0] - 1) % 3
        if (self.table[row][col].check_space([move[1], move[2]])):
            return True
        else:
            return False

    def check_win_row(self, row_num):
        if ((self.table[row_num][0].get_win_x() and 
             self.table[row_num][1].get_win_x() and
             self.table[row_num][2].get_win_x()) or 
            (self.table[row_num][0].get_win_o() and 
             self.table[row_num][1].get_win_o() and 
             self.table[row_num][2].get_win_o()) ):
            return True
        else:
            return False

    def check_win_col(self, col_num):
        if ((self.table[0][col_num].get_win_x() and 
             self.table[1][col_num].get_win_x() and
             self.table[2][col_num].get_win_x()) or 
            (self.table[0][col_num].get_win_o() and 
             self.table[1][col_num].get_win_o() and 
             self.table[2][col_num].get_win_o()) ):
            return True
        else:
            return False

    def check_win_diag1(self):
        if ((self.table[0][0].get_win_x() and 
             self.table[1][1].get_win_x() and
             self.table[2][2].get_win_x()) or 
            (self.table[0][0].get_win_o() and 
             self.table[1][1].get_win_o() and 
             self.table[2][2].get_win_o()) ):
            return True
        else:
            return False

    def check_win_diag2(self):
        if ((self.table[2][0].get_win_x() and 
             self.table[1][1].get_win_x() and
             self.table[0][2].get_win_x()) or 
            (self.table[2][0].get_win_o() and 
             self.table[1][1].get_win_o() and 
             self.table[0][2].get_win_o()) ):
            return True
        else:
            return False

    def check_game(self):
        for row in self.table:
            for slate in row:
                dummy = slate.check_game()

        for k in range(0,3):
            if (self.check_win_row(k) == True and (self.table[k][0].get_win_x() or self.table[k][0].get_win_o())):
                if (self.table[k][0].get_win_x()):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
            elif (self.check_win_col(k) == True and (self.table[0][k].get_win_x() or self.table[0][k].get_win_o())):
                if (self.table[0][k].get_win_x()):
                    self.won_x = True
                    self.make_xo(0)
                else:
                    self.won_o = True
                    self.make_xo(1)
            elif ((self.check_win_diag1() == True or self.check_win_diag2() == True) and (self.table[1][1].get_win_x() or self.table[1][1].get_win_o())):
                if (self.table[1][1].get_win_x()):
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

    #Make sure move is a three dimensional vector
    def place_x(self, move):
        row = int((move[0] - 1) / 3)
        col = (move[0] - 1) % 3
        self.table[row][col].place_x([move[1], move[2]])
        return

    def place_o(self, move):
        row = int((move[0] - 1) / 3)
        col = (move[0] - 1) % 3
        self.table[row][col].place_o([move[1], move[2]])
        return

    def make_xo(self, i):
        if (i % 2 == 0):
            for row in self.table:
                for slate in row:
                    slate.make_xo(i)
        else:
            for row in self.table:
                for slate in row:
                    slate.make_xo(i)
        return

t1 = Table()
t2 = Table()
t3 = Table()
t4 = Table()
t5 = Table()
t6 = Table()
t7 = Table()
t8 = Table()
t9 = Table()

main_wall = [ [t1, t2, t3], [t4, t5, t6], [t7, t8, t9] ]

def print_wall(wall):
    a = 0
    b = 0
    c = 0
    for row in wall:
        table1 = row[0].print_table()
        table2 = row[1].print_table()
        table3 = row[2].print_table()

        for m in range(0,3):
            for n in range(0,3):
                for o in range(0,3):
                    print(table1[m][0][n][0][o] + " | " + table1[m][0][n][1][o] + " | " + table1[m][0][n][2][o] + " || " +
                          table1[m][1][n][0][o] + " | " + table1[m][1][n][1][o] + " | " + table1[m][1][n][2][o] + " || " +
                          table1[m][2][n][0][o] + " | " + table1[m][2][n][1][o] + " | " + table1[m][2][n][2][o] + "  |||  " +
                          table2[m][0][n][0][o] + " | " + table2[m][0][n][1][o] + " | " + table2[m][0][n][2][o] + " || " +
                          table2[m][1][n][0][o] + " | " + table2[m][1][n][1][o] + " | " + table2[m][1][n][2][o] + " || " +
                          table2[m][2][n][0][o] + " | " + table2[m][2][n][1][o] + " | " + table2[m][2][n][2][o] + "  |||  " +
                          table3[m][0][n][0][o] + " | " + table3[m][0][n][1][o] + " | " + table3[m][0][n][2][o] + " || " +
                          table3[m][1][n][0][o] + " | " + table3[m][1][n][1][o] + " | " + table3[m][1][n][2][o] + " || " +
                          table3[m][2][n][0][o] + " | " + table3[m][2][n][1][o] + " | " + table3[m][2][n][2][o])
                if (c < 2):
                    print("--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------" + "  |||  "
                          + "--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------" + "  |||  "
                          + "--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------" + " || "
                          + "--------------------+---------------------+--------------------")
                    c += 1
            c = 0
            if (b < 2):
                print("=========================================================================================================================================================================================================" + 
                      "=========================================================================================================================================================================================================" + 
                      "=========================================================================================================================================================================================================")
                b += 1
        c = 0
        b = 0
        if (a < 2):
            print("=========================================================================================================================================================================================================" + 
                  "=========================================================================================================================================================================================================" + 
                  "=========================================================================================================================================================================================================")
            print("=========================================================================================================================================================================================================" + 
                  "=========================================================================================================================================================================================================" + 
                  "=========================================================================================================================================================================================================")
            a += 1
    return

def w_check_win_row(wall, row_num):
    if ((wall[row_num][0].get_win_x() and
         wall[row_num][1].get_win_x() and
         wall[row_num][2].get_win_x()) or
        (wall[row_num][0].get_win_o() and
         wall[row_num][1].get_win_o() and
         wall[row_num][2].get_win_o())):
        return True
    else:
        return False

def w_check_win_col(wall, col_num):
    if ((wall[0][col_num].get_win_x() and
         wall[1][col_num].get_win_x() and
         wall[2][col_num].get_win_x()) or
        (wall[0][col_num].get_win_o() and
         wall[1][col_num].get_win_o() and
         wall[2][col_num].get_win_o())):
        return True
    else:
        return False

def w_check_win_diag1(wall):
    if ((wall[0][0].get_win_x() and
         wall[1][1].get_win_x() and
         wall[2][2].get_win_x()) or
        (wall[0][0].get_win_o() and
         wall[1][1].get_win_o() and
         wall[2][2].get_win_o())):
        return True
    else:
        return False

def w_check_win_diag2(wall):
    if ((wall[2][0].get_win_x() and
         wall[1][1].get_win_x() and
         wall[0][2].get_win_x()) or
        (wall[2][0].get_win_o() and
         wall[1][1].get_win_o() and
         wall[0][2].get_win_o())):
        return True
    else:
        return False

def check_table(wall, move):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if (wall[row][col].get_win_x() or wall[row][col].get_win_o()):
        return False
    else:
        return True

def check_game(wall, move, i):
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    wall[row][col].check_game()
    if ((wall[row][col].get_win_x()) or (wall[row][col].get_win_o())):
        wall[row][col].make_xo(i)

    for m in range(0,3):
        if ((w_check_win_row(wall, m) == True)):
            return False
        elif ((w_check_win_col(wall, m) == True)):
            return False
        elif ((w_check_win_diag1(wall) == True) or (w_check_win_diag2(wall) == True)):
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

###################################################
##############     Main Game      #################
###################################################

i = 0
game = True
cur_move1 = 0
cur_move2 = 0
cur_move3 = 0
os.system("cls")
while(game):
    print_wall(main_wall)
    if (i % 2 == 0):
        print("It is Player X's Turn")
    else:
        print("It is Player O's Turn")
    print("You are playing in Table " + str(cur_move1))
    print("You are playing in Slate " + str(cur_move2))
    print("You are playing in Board " + str(cur_move3))
    if (cur_move1 == 0 or cur_move1 == -1):
        cur_move1 = input("Please Choose Your Table: ")
        cur_move2 = input("Please Choose Your Slate: ")
        cur_move3 = input("Please Choose Your Board: ")
        cur_move4 = input("Please Choose Your Space: ")
        cur_move1 = check_input(cur_move1)
        cur_move2 = check_input(cur_move2)
        cur_move3 = check_input(cur_move3)
        cur_move4 = check_input(cur_move4)
    elif (cur_move1 != 0 and (cur_move2 == 0 or cur_move2 == -1)):
        cur_move2 = input("Please Choose Your Slate: ")
        cur_move3 = input("Please Choose Your Board: ")
        cur_move4 = input("Please Choose Your Space: ")
        cur_move2 = check_input(cur_move2)
        cur_move3 = check_input(cur_move3)
        cur_move4 = check_input(cur_move4)
    elif (cur_move1 != 0 and cur_move2 != 0 and (cur_move3 == 0 or cur_move3 == -1)):
        cur_move3 = input("Please Choose Your Board: ")
        cur_move4 = input("Please Choose Your Space: ")
        cur_move3 = check_input(cur_move3)
        cur_move4 = check_input(cur_move4)
    else:
        cur_move4 = input("Please Choose Your Space: ")
        cur_move4 = check_input(cur_move4)
    cur_move = [int(cur_move1), int(cur_move2), int(cur_move3), int(cur_move4)]
    w_row = int((cur_move[0] - 1) / 3)
    w_col = (cur_move[0] - 1) % 3
    t_row = int((cur_move[1] - 1) / 3)
    t_col = (cur_move[1] - 1) % 3
    if (cur_move1 == -1 or cur_move2 == -1 or cur_move3 == -1 or cur_move4 == -1):
        os.system("cls")
        print("Try Again")
    elif (main_wall[w_row][w_col].check_space([cur_move[1],cur_move[2], cur_move[3]]) and
          main_wall[w_row][w_col].check_board([cur_move[1], cur_move[2]]) and
          main_wall[w_row][w_col].check_slate(cur_move[1]) and
          check_table(main_wall, cur_move[0])):
        #print(cur_move)
        #print(t_row, t_col)
        if (i % 2 == 0):
            main_wall[w_row][w_col].place_x([cur_move[1],cur_move[2],cur_move[3]])
        else:
            main_wall[w_row][w_col].place_o([cur_move[1],cur_move[2],cur_move[3]])

        game = check_game(main_wall, cur_move[0], i)

        if (check_table(main_wall, cur_move[1])):
            if (main_wall[t_row][t_col].check_slate(cur_move[2])):
                if (main_wall[t_row][t_col].check_board([cur_move[2],cur_move[3]])):
                    cur_move1 = cur_move2
                    cur_move2 = cur_move3
                    cur_move3 = cur_move4
                else:
                    cur_move1 = cur_move2
                    cur_move2 = cur_move3
                    cur_move3 = 0
            else:
                cur_move1 = cur_move2
                cur_move2 = 0
        else:
            cur_move1 = 0
        i += 1
        os.system("cls")
    elif (not check_table(main_wall, cur_move[0])):
        cur_move1 = 0
        os.system("cls")
        print("Try Again")
    elif (not main_wall[w_row][w_col].check_slate(cur_move[1])):
        cur_move2 = 0
        os.system("cls")
        print("Try Again")
    elif (not main_wall[w_row][w_col].check_board([cur_move[1],cur_move[2]])):
        cur_move3 = 0
        os.system("cls")
        print("Try Again")
    else:
        os.system("cls")
        print("Try Again")

print_wall(main_wall)
if ((i - 1) % 2 == 0):
    print("Congrats! Player X Won!")
else:
    print("Congrats! Player O Won!")
print("Won in " + str(i + 2) + " moves.")