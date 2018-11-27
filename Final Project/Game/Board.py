class Board:
    def __init__(self):
        self.contents = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.won = False
        self.win_token = 'none'
        self.win_condition_pos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                                 [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[2,0],[1,1],[0,2]],
                                 [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]]]

    def __is_played(self, move_pos):
        # Pass in a list for the pos
        return (self.contents[move_pos[0]][move_pos[1]] != ' ')

    def __check_for_draw(self):
        return ((' ' not in self.contents[0]) and (' ' not in self.contents[1]) and (' ' not in self.contents[2]))

    def __check_for_win(self):
        for condition in self.win_condition_pos:
            pos1 = condition[0]
            pos2 = condition[1]
            pos3 = condition[2]
            board = self.contents
            if board[pos1[0]][pos1[1]] == board[pos2[0]][pos2[1]] == board[pos3[0]][pos3[1]] != ' ':
                self.won = True
                self.win_token = board[pos1[0]][pos1[1]]
        return self.won

    def __check_for_end(self):
        win = self.__check_for_win()
        draw = self.__check_for_draw()
        if win == True and draw == False:
            print("Player %s won" % self.win_token)
            return True
        elif win == False and draw == True:
            print("Game is a draw")
            return True
        return False

    def __display_row(self, row):
        pos = 0
        print(" ", end='')
        for col in row:
            print(col, end='')
            if pos != 2:
                print(' │ ', end='')
            pos += 1

    def display_board(self):
        row_num = 0
        for row in self.contents:
            self.__display_row(row)
            if row_num != 2:
                print("\n───┼───┼───", end='')
            row_num += 1
            print()

    def __make_move(self, move_pos, token):
        # Pass in a tuple for the pos
        move_made = False
        if self.__is_played(move_pos):
            print("Sorry, that spot has been played")
        else:
            self.contents[move_pos[0]][move_pos[1]] = token
            move_made = True
        return move_made

    def update_board(self, move_pos, token):
        move_done = self.__make_move(move_pos, token)
        while move_done != True:
            move_done = self.__make_move(move_pos, token)
        return self.__check_for_end()

def play_game(Board, token1, token2):
    tokens = [token1, token2]
    while test.won != True:
        for player in [1, 2]:
            print()
            test.display_board()
            print("It's player %d's turn" % player)
            xcoord = int(input("\nEnter the x-coordinate of spot going from the left: "))
            ycoord = int(input("Enter the y-coordinate of spot going from the top: "))
            done = test.update_board([ycoord,xcoord], tokens[player - 1])
            if done == True:
                input()
                break

if __name__ == "__main__":
    player1_token = 'x'
    player2_token = 'o'
    test = Board()
    play_game(test, player1_token, player2_token)
    