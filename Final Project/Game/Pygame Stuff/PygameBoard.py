import pygame

class TestingBoard:
    def __init__(self, ttt, startx, starty, colWidth, bgColor=(250, 250, 250)):
        self.XO   = "X"   # track whose turn it is; X goes first
        self.grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.win_condition_pos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                   [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[2,0],[1,1],[0,2]],
                   [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]]]
        self.background = None
        self.won = None
        self.win_token = ' '

    # def initBoard(self, ttt, startx, starty, colWidth, bgColor=(250, 250, 250)):
        # set up the background surface
        self.colWidth = colWidth
        self.startX = startx
        self.startY = starty
        self.board_size = ttt.get_size()
        self.background = pygame.Surface(self.board_size)
        self.background = self.background.convert()
        self.background.fill(bgColor)

        # draw the grid lines
        # vertical lines...
        pygame.draw.line (self.background, (0,0,0), (startx + self.colWidth, starty), (startx + self.colWidth, starty + (self.colWidth * 3)), 2)
        pygame.draw.line (self.background, (0,0,0), (startx + (self.colWidth * 2), starty), (startx + (self.colWidth * 2), starty + (self.colWidth * 3)), 2)

        # horizontal lines...
        pygame.draw.line (self.background, (0,0,0), (startx, starty + self.colWidth), (startx + (self.colWidth * 3), starty + self.colWidth), 2)
        pygame.draw.line (self.background, (0,0,0), (startx, starty + (self.colWidth * 2)), (startx + (self.colWidth * 3), starty + (self.colWidth * 2)), 2)

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
                if self.won is None:
                    # Drawing lineshit
                    startx = (pos1[1] + 1) * self.colWidth - (self.colWidth / 2)
                    starty = (pos1[0] + 1) * self.colWidth - (self.colWidth / 2)
                    endx = (pos3[1] + 1) * self.colWidth - (self.colWidth / 2)
                    endy = (pos3[0] + 1) * self.colWidth - (self.colWidth / 2)
                    pygame.draw.line (self.background, (250,0,0), (startx + self.startX, starty + self.startY), (endx + self.startX, endy + self.startY), 4)
                self.won = True
                self.win_token = board[pos1[0]][pos1[1]]
        return self.won

    def drawStatus (self, board):
        # determine the status message
        if (self.won is None):
            message = self.XO + "'s turn"
        else:
            message = self.win_token + " won!"

        # render the status message
        font = pygame.font.Font(None, 24)
        text = font.render(message, 1, (10, 10, 10))

        # copy the rendered message onto the board
        board.fill ((250, 250, 250), (self.startX, (self.startY + 300), 300, 25))
        board.blit(text, ((self.startX + 10), (self.startY + 300)))
    
    def showBoard (self, ttt):
        self.drawStatus (self.background)
        ttt.blit (self.background, (0, 0))
        pygame.display.flip()

    def boardPos (self, mouseX, mouseY):
        # determine the row the user clicked
        if (mouseY < (self.colWidth + self.startY)):
            row = 0
        elif (mouseY < ((self.colWidth * 2) + self.startY)):
            row = 1
        else:
            row = 2
        # determine the column the user clicked
        if (mouseX < (self.colWidth + self.startX)):
            col = 0
        elif (mouseX < ((self.colWidth * 2) + self.startX)):
            col = 1
        else:
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
            pygame.draw.circle (self.background, (0,0,0), (centerX, centerY), int(piece_size * 2), 2)
        else:
            pygame.draw.line (self.background, (0,0,0), (centerX - piece_size, centerY - piece_size), \
                             (centerX + piece_size, centerY + piece_size), 2)
            pygame.draw.line (self.background, (0,0,0), (centerX + piece_size, centerY - piece_size), \
                             (centerX - piece_size, centerY + piece_size), 2)

        # mark the space as used
        self.grid[boardRow][boardCol] = Piece
    
    def clickBoard(self):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        (row, col) = self.boardPos(mouseX, mouseY)

        # make sure no one's used this space
        if self.__is_played((row, col)) == True:
            return

        # draw an X or O
        self.drawMove(row, col, self.XO)

        # toggle XO to the other player's move
        if (self.XO == "X"):
            self.XO = "O"
        else:
            self.XO = "X"

    def gameWon(self):
        return self.__check_for_draw() or self.__check_for_win()

pygame.init()
ttt = pygame.display.set_mode ((600, 625))
pygame.display.set_caption ('Tic-Tac-Toe')

board_size = ttt.get_size()
background = pygame.Surface(board_size)
background = background.convert()
background.fill((250, 250, 250))

boards = [[TestingBoard(ttt, 0, 0, 50), TestingBoard(ttt, 150, 0, 50), TestingBoard(ttt, 300, 0, 50)]]

# main event loop
running = 1
while (running == 1):
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = 0
        elif event.type is pygame.MOUSEBUTTONDOWN:
            board_select = pygame.mouse.get_pos()
            if board_select[0] < 150:
                if board_select[1] < 150:
                    boards[0][0].clickBoard()
                elif board_select[1] < 300:
                    pass
                else:
                    pass
            elif board_select[0] < 300:
                if board_select[1] < 150:
                    boards[0][1].clickBoard()
                elif board_select[1] < 300:
                    pass
                else:
                    pass
            else:
                if board_select[1] < 150:
                    boards[0][2].clickBoard()
                elif board_select[1] < 300:
                    pass
                else:
                    pass
        for row in boards:
            for board in row:
                board.gameWon()
                # if board.won == True:
                #     running = 0
                # update the display
                board.showBoard(ttt)