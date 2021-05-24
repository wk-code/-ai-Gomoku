import pygame


class ChessBoard:
    def __init__(self, settings, screen):
        self.rect = pygame.Rect((settings.board_left, settings.board_top),
                                (settings.board_width, settings.board_height))
        self.settings = settings
        self.screen = screen
        self.color = (249, 214, 91)

        self.line_color = (0, 0, 0)
        self.line_num = settings.line_num
        self.line_length = settings.line_length
        self.line_initial_left = settings.line_initial_left
        self.line_initial_top = settings.line_initial_top

    def draw_board(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        width = self.settings.width
        num = self.line_num
        left = self.line_initial_left
        top = self.line_initial_top
        length = self.line_length
        color = self.line_color

        # 绘制棋盘上的线
        for i in range(num):
            pygame.draw.line(self.screen, color, (left + i * width, top), (left + i*width, top + length), 1)

        for i in range(num):
            pygame.draw.line(self.screen, color, (left, top + i * width), (left + length, top + i * width), 1)

        # 绘制棋盘上的五个小点（星位）
        pygame.draw.circle(self.screen, color, (left + num//2 * width, top + num//2 * width), 4)
        pygame.draw.circle(self.screen, color, (left + num//4 * width, top + num//4 * width), 4)
        pygame.draw.circle(self.screen, color, (left + length - num//4 * width, top + num//4 * width), 4)
        pygame.draw.circle(self.screen, color, (left + num//4 * width, top + length - num//4 * width), 4)
        pygame.draw.circle(self.screen, color, (left + length - num//4 * width, top + length - num//4 * width), 4)
