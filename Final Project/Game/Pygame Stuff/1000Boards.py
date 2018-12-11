import pygame
import math

class TestingBoard:
    def __init__(self, ttt, startx, starty, colWidth, background):
        self.XO   = "X"   # track whose turn it is; X goes first
        self.grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.win_condition_pos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                   [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],
                   [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]]]
        self.background = background
        self.won = False
        self.win_token = ' '
        self.colWidth = colWidth
        self.startX = startx
        self.startY = starty
        self.center_coords = self.return_center()

        # draw the grid lines
        # vertical lines...
        pygame.draw.line (self.background, (214,214,214), (startx + self.colWidth, starty), (startx + self.colWidth, starty + (self.colWidth * 3)), 4)
        pygame.draw.line (self.background, (214,214,214), (startx + (self.colWidth * 2), starty), (startx + (self.colWidth * 2), starty + (self.colWidth * 3)), 4)

        # horizontal lines...
        pygame.draw.line (self.background, (214,214,214), (startx, starty + self.colWidth), (startx + (self.colWidth * 3), starty + self.colWidth), 4)
        pygame.draw.line (self.background, (214,214,214), (startx, starty + (self.colWidth * 2)), (startx + (self.colWidth * 3), starty + (self.colWidth * 2)), 4)

    def __is_played(self, move_pos):
        # Pass in a list for the pos
        return (self.grid[move_pos[0]][move_pos[1]] != ' ')

    def __check_for_draw(self):
        return ((' ' not in self.grid[0]) and (' ' not in self.grid[1]) and (' ' not in self.grid[2]))

    def __check_for_win(self):
        for condition in self.win_condition_pos:
            pos1 = condition[0]
            pos2 = condition[1]
            pos3 = condition[2]
            board = self.grid
            if board[pos1[0]][pos1[1]] == board[pos2[0]][pos2[1]] == board[pos3[0]][pos3[1]] != ' ':
                if self.won is False:
                    # Drawing lineshit
                    startx = (pos1[1] + 1) * self.colWidth - (self.colWidth / 2)
                    starty = (pos1[0] + 1) * self.colWidth - (self.colWidth / 2)
                    endx = (pos3[1] + 1) * self.colWidth - (self.colWidth / 2)
                    endy = (pos3[0] + 1) * self.colWidth - (self.colWidth / 2)
                    # TODO Add in change of color for win line
                    pygame.draw.line (self.background, (250,0,0), (startx + self.startX, starty + self.startY), (endx + self.startX, endy + self.startY), 4)
                self.won = True
                self.win_token = board[pos1[0]][pos1[1]]
        return self.won

    def return_center(self):
        return (self.startX + (self.colWidth * 1.5), self.startY + (self.colWidth * 1.5))
    
    def showBoard (self, ttt):
        ttt.blit (self.background, (0, 0))
        pygame.display.flip()

    def boardPos (self, mouseX, mouseY):
        row = None
        col = None
        # determine the row the user clicked
        if ((self.startY) < mouseY < ((self.colWidth * 1) + self.startY)):
            row = 0
        elif ((self.startY) < mouseY < ((self.colWidth * 2) + self.startY)):
            row = 1
        elif ((self.startY) < mouseY < ((self.colWidth * 3) + self.startY)):
            row = 2
        # determine the column the user clicked
        if ((self.startX) < mouseX < ((self.colWidth * 1) + self.startX)):
            col = 0
        elif ((self.startX) < mouseX < ((self.colWidth * 2) + self.startX)):
            col = 1
        elif ((self.startX) < mouseX < ((self.colWidth * 3) + self.startX)):
            col = 2

        # return the tuple containg the row & column
        return (row, col)
    
    def drawMove (self, boardRow, boardCol, Piece):
        # determine the center of the square
        centerX = int(((boardCol) * self.colWidth) + (self.colWidth / 2) + self.startX)
        centerY = int(((boardRow) * self.colWidth) + (self.colWidth / 2) + self.startY)

        piece_size = self.colWidth / 4.54545454545454

        # draw the appropriate piece
        if (Piece == 'O'):
            pygame.draw.circle (self.background, (214,214,214), (centerX, centerY), int(piece_size * 2), 2)
        else:
            pygame.draw.line (self.background, (214,214,214), (centerX - piece_size, centerY - piece_size), \
                             (centerX + piece_size, centerY + piece_size), 2)
            pygame.draw.line (self.background, (214,214,214), (centerX + piece_size, centerY - piece_size), \
                             (centerX - piece_size, centerY + piece_size), 2)

        # mark the space as used
        self.grid[boardRow][boardCol] = Piece
    
    def clickBoard(self, piece):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        (row, col) = self.boardPos(mouseX, mouseY)

        # make sure no one's used this space
        # TODO Fix return of None if space is played
        if self.__is_played((row, col)) == True:
            return

        # draw an X or O
        self.drawMove(row, col, piece)

        return (row, col)

    def gameWon(self):
        return self.__check_for_draw() or self.__check_for_win()

class BigBoard:
    def __init__(self, num_boards, col_width, bg_color=(250,250,250)):
        self.col_width = col_width
        self.num_boards = num_boards
        self.bg_color = bg_color
        self.boards = []
        self.won = False
        self.XO = 'X'
        self.XOColor = ()
        self.XColor = (250,0,0)
        self.YColor = (15,2,255)
        self.win_condition_pos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                   [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[2,0],[1,1],[0,2]],
                   [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]]]

        pygame.init()
        
    def __init_board(self, screen_size, num_boards):
        self.ttt = pygame.display.set_mode((screen_size))
        
        self.board_size = self.ttt.get_size()
        self.background = pygame.Surface(self.board_size)
        self.background = self.background.convert()
        self.background.fill(self.bg_color)

        # Board Size Thingy
        self.new_size = self.board_size[0] / num_boards
        self.length = self.board_size[0]

        # Vertical and Horizontal lines
        for i in range(int(num_boards)):
            pygame.draw.line(self.background, (214,214,214), (self.new_size * (i + 1), 0), (self.new_size * (i + 1), self.length), 6)
            pygame.draw.line(self.background, (214,214,214), (0, self.new_size * (i + 1)), (self.length, self.new_size * (i + 1)), 6)

    def __gen_boards(self):
        num_boards = math.sqrt(self.num_boards)
        num_cols = num_boards * 4
        num_rows = num_cols
        screen_length = int((num_cols + 1) * self.col_width)
        self.__init_board((screen_length, screen_length), num_boards)
        self.col_width = self.board_size[0] / num_cols
        startY = self.col_width / 2
        for i in range(int(num_rows) + 1):
            new_row = []
            startX = self.col_width / 2
            for j in range(int(num_rows) + 1):
                new_row.append(TestingBoard(self.ttt, startX, startY, self.col_width, self.background))
                startX += (self.col_width * 4)
            self.boards.append(new_row)
            startY += (self.col_width * 4)

    def __within_tol(self, val, start, stop):
        # print("Start: %d < Val: %d < End: %d" % (start, val, stop))
        return start < val < stop

    def __play_board(self, board_pos):
        new_pos = self.boards[board_pos[0]][board_pos[1]].clickBoard()
        return new_pos

    def game_won(self):
        for condition in self.win_condition_pos:
            pos1 = condition[0]
            pos2 = condition[1]
            pos3 = condition[2]
            board = self.boards
            if board[pos1[0]][pos1[1]].won == board[pos2[0]][pos2[1]].won == board[pos3[0]][pos3[1]].won != False and \
               board[pos1[0]][pos1[1]].win_token == board[pos2[0]][pos2[1]].win_token == board[pos3[0]][pos3[1]].win_token:
                start_pos = board[pos1[0]][pos1[1]].return_center()
                end_pos = board[pos3[0]][pos3[1]].return_center()
                pygame.draw.line(self.background, self.XColor, (start_pos[0], start_pos[1]), (end_pos[0], end_pos[1]), 8)
                self.won = True
                self.win_token = board[pos1[0]][pos1[1]].win_token
        return self.won

    def play_game(self):
        self.__gen_boards()
        # main event loop
        board_pos = (1,1)
        running = 1
        while (running == 1):
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    running = 0
                elif event.type is pygame.MOUSEBUTTONDOWN:
                    # new_pos = pygame.mouse.get_pos()
                    # print("Board pos:", self.boards[board_pos[0]][board_pos[1]].self_pos)
                    # print("New pos:", new_pos)
                    if (self.__within_tol(new_pos[0], self.boards[board_pos[0]][board_pos[1]].startX, self.boards[board_pos[0]][board_pos[1]].startX + (self.col_width * 3))) and \
                       (self.__within_tol(new_pos[1], self.boards[board_pos[0]][board_pos[1]].startY, self.boards[board_pos[0]][board_pos[1]].startY + (self.col_width * 3))):
                        board_pos = self.boards[board_pos[0]][board_pos[1]].clickBoard(self.XO)
                    
                        # toggle XO to the other player's move
                        if (self.XO == "X"):
                            self.XO = "O"
                            self.XOColor = self.YColor
                        else:
                            self.XO = "X"
                            self.XOColor = self.XColor
                    else:
                        print("oops")
                    # print("Next pos:", board_pos)

            for row in self.boards:
                for board in row:
                    board.gameWon()
                    if self.won == True:
                        running = 0
                    # update the display
                    # TODO Add turn display and proper win/draw message
                    board.showBoard(self.ttt)
            self.game_won()
        else:
            print("%s Won" % self.XO)

big_board = BigBoard(36, 25, bg_color=(73,73,73))
big_board.play_game()