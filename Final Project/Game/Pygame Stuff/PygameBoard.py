import pygame as pygame

class Board:
    def __init__(self, window):
        self.contents = [[None, None, None], [None, None, None], [None, None, None]]
        self.win_condition_pos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
                                 [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[2,0],[1,1],[0,2]],
                                 [[0,0],[1,1],[2,2]], [[2,0],[1,1],[0,2]]]
        self.won = False
        self.player_tokens = ['X', 'O']
        self.background = pygame.Surface(window.get_size())
        self.background.convert()
        self.background.fill((250, 250, 250))

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Tic-tac-toe")

running = True

while (running == True):
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
        elif event.type is pygame.MOUSEBUTTONDOWN:
            pass
