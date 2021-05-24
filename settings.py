import pygame


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 520
        self.bg_color = (230, 230, 230)
        self.img = pygame.image.load("图标.jpg")
        self.board_left = 10
        self.board_top = 10
        self.board_width = 500
        self.board_height = 500
        self.line_num = 15
        self.line_length = 452
        self.line_initial_left = 34
        self.line_initial_top = 33
        self.width = self.board_width / self.line_num - 1

        self.black_img = pygame.image.load("black.png")
        self.black_img = pygame.transform.smoothscale(self.black_img, (30, 30))
        self.white_img = pygame.image.load("white.png")
        self.white_img = pygame.transform.smoothscale(self.white_img, (30, 30))
        self.turn = True  # true代表黑棋，false代表白棋
        self.player_turn = 2

        self.winner = 0  # 0表示没有赢家，1表示黑棋赢，2表示白棋赢
        self.stat = False  # false代表游戏未开始，true表示游戏已经开始

        self.max_x = -1
        self.max_y = -1
        self.min_x = 15
        self.min_y = 15

    def setTurn(self):
        self.turn = not self.turn
